from fastapi import APIRouter, HTTPException # type: ignore
from app.models.transaction import transactionRequest, transactionResponse
from app.services.rule_engine import rule_engine
from app.services.ML_engine import MLEngine
from app.services.idempotency import check_idempotency
from app.core.config import Settings

router = APIRouter()
rule_engine_instance = rule_engine()
ml_engine_instance = MLEngine()

@router.post("/transaction", response_model=transactionResponse)
    def process_transaction(transaction_data: transactionRequest):  
        if not check_idempotency(tx.transaction_data.transaction_id):
            raise HTTPException(status_code=409, detail="Duplicate transaction")
         rule_risk,rules=rule_engine.evaluate_transaction(transaction_data)
         ml_risk,ml_score=ml_engine_instance.evaluate_transaction(transaction_data)     
         
         final_risk=max(rule_risk,ml_risk)
        status= APPROVE if not final_risk else REJECT
            final_risk = rule_risk or (ml_score > Settings().ML_THRESHOLD)
            status = "REJECT" if final_risk else "APPROVE"
            response = transactionResponse(
                transaction_id=transaction_data.transaction_id,
                is_fraud=final_risk,
                score=ml_score")
            return transactionResponse(transaction_id=transaction_data.transaction_id, is_fraud=final_risk, score=ml_score)
"""
Type annotations for bedrock-runtime service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_bedrock_runtime/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_bedrock_runtime.type_defs import AppliedGuardrailDetailsTypeDef

    data: AppliedGuardrailDetailsTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from collections.abc import Mapping, Sequence
from datetime import datetime
from typing import IO, Any, Union

from botocore.eventstream import EventStream
from botocore.response import StreamingBody

from .literals import (
    AsyncInvokeStatusType,
    AudioFormatType,
    ConversationRoleType,
    DocumentFormatType,
    GuardrailActionType,
    GuardrailAutomatedReasoningLogicWarningTypeType,
    GuardrailContentFilterConfidenceType,
    GuardrailContentFilterStrengthType,
    GuardrailContentFilterTypeType,
    GuardrailContentPolicyActionType,
    GuardrailContentQualifierType,
    GuardrailContentSourceType,
    GuardrailContextualGroundingFilterTypeType,
    GuardrailContextualGroundingPolicyActionType,
    GuardrailConverseContentQualifierType,
    GuardrailConverseImageFormatType,
    GuardrailImageFormatType,
    GuardrailOriginType,
    GuardrailOutputScopeType,
    GuardrailOwnershipType,
    GuardrailPiiEntityTypeType,
    GuardrailSensitiveInformationPolicyActionType,
    GuardrailStreamProcessingModeType,
    GuardrailTopicPolicyActionType,
    GuardrailTraceType,
    GuardrailWordPolicyActionType,
    ImageFormatType,
    PerformanceConfigLatencyType,
    ServiceTierTypeType,
    SortOrderType,
    StopReasonType,
    ToolResultStatusType,
    ToolUseTypeType,
    TraceType,
    VideoFormatType,
)

if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict


__all__ = (
    "AppliedGuardrailDetailsTypeDef",
    "ApplyGuardrailRequestTypeDef",
    "ApplyGuardrailResponseTypeDef",
    "AsyncInvokeOutputDataConfigTypeDef",
    "AsyncInvokeS3OutputDataConfigTypeDef",
    "AsyncInvokeSummaryTypeDef",
    "AudioBlockOutputTypeDef",
    "AudioBlockTypeDef",
    "AudioBlockUnionTypeDef",
    "AudioSourceOutputTypeDef",
    "AudioSourceTypeDef",
    "AudioSourceUnionTypeDef",
    "BidirectionalInputPayloadPartTypeDef",
    "BidirectionalOutputPayloadPartTypeDef",
    "BlobTypeDef",
    "CachePointBlockTypeDef",
    "CitationGeneratedContentTypeDef",
    "CitationLocationTypeDef",
    "CitationOutputTypeDef",
    "CitationSourceContentDeltaTypeDef",
    "CitationSourceContentTypeDef",
    "CitationTypeDef",
    "CitationUnionTypeDef",
    "CitationsConfigTypeDef",
    "CitationsContentBlockOutputTypeDef",
    "CitationsContentBlockTypeDef",
    "CitationsContentBlockUnionTypeDef",
    "CitationsDeltaTypeDef",
    "ContentBlockDeltaEventTypeDef",
    "ContentBlockDeltaTypeDef",
    "ContentBlockOutputTypeDef",
    "ContentBlockStartEventTypeDef",
    "ContentBlockStartTypeDef",
    "ContentBlockStopEventTypeDef",
    "ContentBlockTypeDef",
    "ContentBlockUnionTypeDef",
    "ConverseMetricsTypeDef",
    "ConverseOutputTypeDef",
    "ConverseRequestTypeDef",
    "ConverseResponseTypeDef",
    "ConverseStreamMetadataEventTypeDef",
    "ConverseStreamMetricsTypeDef",
    "ConverseStreamOutputTypeDef",
    "ConverseStreamRequestTypeDef",
    "ConverseStreamResponseTypeDef",
    "ConverseStreamTraceTypeDef",
    "ConverseTokensRequestTypeDef",
    "ConverseTraceTypeDef",
    "CountTokensInputTypeDef",
    "CountTokensRequestTypeDef",
    "CountTokensResponseTypeDef",
    "DocumentBlockOutputTypeDef",
    "DocumentBlockTypeDef",
    "DocumentBlockUnionTypeDef",
    "DocumentCharLocationTypeDef",
    "DocumentChunkLocationTypeDef",
    "DocumentContentBlockTypeDef",
    "DocumentPageLocationTypeDef",
    "DocumentSourceOutputTypeDef",
    "DocumentSourceTypeDef",
    "DocumentSourceUnionTypeDef",
    "ErrorBlockTypeDef",
    "GetAsyncInvokeRequestTypeDef",
    "GetAsyncInvokeResponseTypeDef",
    "GuardrailAssessmentTypeDef",
    "GuardrailAutomatedReasoningFindingTypeDef",
    "GuardrailAutomatedReasoningImpossibleFindingTypeDef",
    "GuardrailAutomatedReasoningInputTextReferenceTypeDef",
    "GuardrailAutomatedReasoningInvalidFindingTypeDef",
    "GuardrailAutomatedReasoningLogicWarningTypeDef",
    "GuardrailAutomatedReasoningPolicyAssessmentTypeDef",
    "GuardrailAutomatedReasoningRuleTypeDef",
    "GuardrailAutomatedReasoningSatisfiableFindingTypeDef",
    "GuardrailAutomatedReasoningScenarioTypeDef",
    "GuardrailAutomatedReasoningStatementTypeDef",
    "GuardrailAutomatedReasoningTranslationAmbiguousFindingTypeDef",
    "GuardrailAutomatedReasoningTranslationOptionTypeDef",
    "GuardrailAutomatedReasoningTranslationTypeDef",
    "GuardrailAutomatedReasoningValidFindingTypeDef",
    "GuardrailConfigurationTypeDef",
    "GuardrailContentBlockTypeDef",
    "GuardrailContentFilterTypeDef",
    "GuardrailContentPolicyAssessmentTypeDef",
    "GuardrailContextualGroundingFilterTypeDef",
    "GuardrailContextualGroundingPolicyAssessmentTypeDef",
    "GuardrailConverseContentBlockOutputTypeDef",
    "GuardrailConverseContentBlockTypeDef",
    "GuardrailConverseContentBlockUnionTypeDef",
    "GuardrailConverseImageBlockOutputTypeDef",
    "GuardrailConverseImageBlockTypeDef",
    "GuardrailConverseImageBlockUnionTypeDef",
    "GuardrailConverseImageSourceOutputTypeDef",
    "GuardrailConverseImageSourceTypeDef",
    "GuardrailConverseImageSourceUnionTypeDef",
    "GuardrailConverseTextBlockOutputTypeDef",
    "GuardrailConverseTextBlockTypeDef",
    "GuardrailConverseTextBlockUnionTypeDef",
    "GuardrailCoverageTypeDef",
    "GuardrailCustomWordTypeDef",
    "GuardrailImageBlockTypeDef",
    "GuardrailImageCoverageTypeDef",
    "GuardrailImageSourceTypeDef",
    "GuardrailInvocationMetricsTypeDef",
    "GuardrailManagedWordTypeDef",
    "GuardrailOutputContentTypeDef",
    "GuardrailPiiEntityFilterTypeDef",
    "GuardrailRegexFilterTypeDef",
    "GuardrailSensitiveInformationPolicyAssessmentTypeDef",
    "GuardrailStreamConfigurationTypeDef",
    "GuardrailTextBlockTypeDef",
    "GuardrailTextCharactersCoverageTypeDef",
    "GuardrailTopicPolicyAssessmentTypeDef",
    "GuardrailTopicTypeDef",
    "GuardrailTraceAssessmentTypeDef",
    "GuardrailUsageTypeDef",
    "GuardrailWordPolicyAssessmentTypeDef",
    "ImageBlockDeltaTypeDef",
    "ImageBlockOutputTypeDef",
    "ImageBlockStartTypeDef",
    "ImageBlockTypeDef",
    "ImageBlockUnionTypeDef",
    "ImageSourceOutputTypeDef",
    "ImageSourceTypeDef",
    "ImageSourceUnionTypeDef",
    "InferenceConfigurationTypeDef",
    "InternalServerExceptionTypeDef",
    "InvokeModelRequestTypeDef",
    "InvokeModelResponseTypeDef",
    "InvokeModelTokensRequestTypeDef",
    "InvokeModelWithBidirectionalStreamInputTypeDef",
    "InvokeModelWithBidirectionalStreamOutputTypeDef",
    "InvokeModelWithBidirectionalStreamRequestTypeDef",
    "InvokeModelWithBidirectionalStreamResponseTypeDef",
    "InvokeModelWithResponseStreamRequestTypeDef",
    "InvokeModelWithResponseStreamResponseTypeDef",
    "ListAsyncInvokesRequestPaginateTypeDef",
    "ListAsyncInvokesRequestTypeDef",
    "ListAsyncInvokesResponseTypeDef",
    "MessageOutputTypeDef",
    "MessageStartEventTypeDef",
    "MessageStopEventTypeDef",
    "MessageTypeDef",
    "MessageUnionTypeDef",
    "ModelStreamErrorExceptionTypeDef",
    "ModelTimeoutExceptionTypeDef",
    "PaginatorConfigTypeDef",
    "PayloadPartTypeDef",
    "PerformanceConfigurationTypeDef",
    "PromptRouterTraceTypeDef",
    "PromptVariableValuesTypeDef",
    "ReasoningContentBlockDeltaTypeDef",
    "ReasoningContentBlockOutputTypeDef",
    "ReasoningContentBlockTypeDef",
    "ReasoningContentBlockUnionTypeDef",
    "ReasoningTextBlockTypeDef",
    "ResponseMetadataTypeDef",
    "ResponseStreamTypeDef",
    "S3LocationTypeDef",
    "SearchResultBlockOutputTypeDef",
    "SearchResultBlockTypeDef",
    "SearchResultBlockUnionTypeDef",
    "SearchResultContentBlockTypeDef",
    "SearchResultLocationTypeDef",
    "ServiceTierTypeDef",
    "ServiceUnavailableExceptionTypeDef",
    "SpecificToolChoiceTypeDef",
    "StartAsyncInvokeRequestTypeDef",
    "StartAsyncInvokeResponseTypeDef",
    "SystemContentBlockTypeDef",
    "SystemToolTypeDef",
    "TagTypeDef",
    "ThrottlingExceptionTypeDef",
    "TimestampTypeDef",
    "TokenUsageTypeDef",
    "ToolChoiceTypeDef",
    "ToolConfigurationTypeDef",
    "ToolInputSchemaTypeDef",
    "ToolResultBlockDeltaTypeDef",
    "ToolResultBlockOutputTypeDef",
    "ToolResultBlockStartTypeDef",
    "ToolResultBlockTypeDef",
    "ToolResultBlockUnionTypeDef",
    "ToolResultContentBlockOutputTypeDef",
    "ToolResultContentBlockTypeDef",
    "ToolResultContentBlockUnionTypeDef",
    "ToolSpecificationTypeDef",
    "ToolTypeDef",
    "ToolUseBlockDeltaTypeDef",
    "ToolUseBlockOutputTypeDef",
    "ToolUseBlockStartTypeDef",
    "ToolUseBlockTypeDef",
    "ToolUseBlockUnionTypeDef",
    "ValidationExceptionTypeDef",
    "VideoBlockOutputTypeDef",
    "VideoBlockTypeDef",
    "VideoBlockUnionTypeDef",
    "VideoSourceOutputTypeDef",
    "VideoSourceTypeDef",
    "VideoSourceUnionTypeDef",
    "WebLocationTypeDef",
)


class AppliedGuardrailDetailsTypeDef(TypedDict):
    guardrailId: NotRequired[str]
    guardrailVersion: NotRequired[str]
    guardrailArn: NotRequired[str]
    guardrailOrigin: NotRequired[list[GuardrailOriginType]]
    guardrailOwnership: NotRequired[GuardrailOwnershipType]


class GuardrailOutputContentTypeDef(TypedDict):
    text: NotRequired[str]


class GuardrailUsageTypeDef(TypedDict):
    topicPolicyUnits: int
    contentPolicyUnits: int
    wordPolicyUnits: int
    sensitiveInformationPolicyUnits: int
    sensitiveInformationPolicyFreeUnits: int
    contextualGroundingPolicyUnits: int
    contentPolicyImageUnits: NotRequired[int]
    automatedReasoningPolicyUnits: NotRequired[int]
    automatedReasoningPolicies: NotRequired[int]


class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]


class AsyncInvokeS3OutputDataConfigTypeDef(TypedDict):
    s3Uri: str
    kmsKeyId: NotRequired[str]
    bucketOwner: NotRequired[str]


class ErrorBlockTypeDef(TypedDict):
    message: NotRequired[str]


class S3LocationTypeDef(TypedDict):
    uri: str
    bucketOwner: NotRequired[str]


BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
BidirectionalOutputPayloadPartTypeDef = TypedDict(
    "BidirectionalOutputPayloadPartTypeDef",
    {
        "bytes": NotRequired[bytes],
    },
)
CachePointBlockTypeDef = TypedDict(
    "CachePointBlockTypeDef",
    {
        "type": Literal["default"],
    },
)


class CitationGeneratedContentTypeDef(TypedDict):
    text: NotRequired[str]


class DocumentCharLocationTypeDef(TypedDict):
    documentIndex: NotRequired[int]
    start: NotRequired[int]
    end: NotRequired[int]


class DocumentChunkLocationTypeDef(TypedDict):
    documentIndex: NotRequired[int]
    start: NotRequired[int]
    end: NotRequired[int]


class DocumentPageLocationTypeDef(TypedDict):
    documentIndex: NotRequired[int]
    start: NotRequired[int]
    end: NotRequired[int]


class SearchResultLocationTypeDef(TypedDict):
    searchResultIndex: NotRequired[int]
    start: NotRequired[int]
    end: NotRequired[int]


class WebLocationTypeDef(TypedDict):
    url: NotRequired[str]
    domain: NotRequired[str]


class CitationSourceContentTypeDef(TypedDict):
    text: NotRequired[str]


class CitationSourceContentDeltaTypeDef(TypedDict):
    text: NotRequired[str]


class CitationsConfigTypeDef(TypedDict):
    enabled: bool


class ReasoningContentBlockDeltaTypeDef(TypedDict):
    text: NotRequired[str]
    redactedContent: NotRequired[bytes]
    signature: NotRequired[str]


class ToolResultBlockDeltaTypeDef(TypedDict):
    text: NotRequired[str]
    json: NotRequired[dict[str, Any]]


ToolUseBlockDeltaTypeDef = TypedDict(
    "ToolUseBlockDeltaTypeDef",
    {
        "input": str,
    },
)
ToolUseBlockOutputTypeDef = TypedDict(
    "ToolUseBlockOutputTypeDef",
    {
        "toolUseId": str,
        "name": str,
        "input": dict[str, Any],
        "type": NotRequired[ToolUseTypeType],
    },
)
ImageBlockStartTypeDef = TypedDict(
    "ImageBlockStartTypeDef",
    {
        "format": ImageFormatType,
    },
)
ToolResultBlockStartTypeDef = TypedDict(
    "ToolResultBlockStartTypeDef",
    {
        "toolUseId": str,
        "type": NotRequired[str],
        "status": NotRequired[ToolResultStatusType],
    },
)
ToolUseBlockStartTypeDef = TypedDict(
    "ToolUseBlockStartTypeDef",
    {
        "toolUseId": str,
        "name": str,
        "type": NotRequired[ToolUseTypeType],
    },
)


class ContentBlockStopEventTypeDef(TypedDict):
    contentBlockIndex: int


class ConverseMetricsTypeDef(TypedDict):
    latencyMs: int


class GuardrailConfigurationTypeDef(TypedDict):
    guardrailIdentifier: NotRequired[str]
    guardrailVersion: NotRequired[str]
    trace: NotRequired[GuardrailTraceType]


class InferenceConfigurationTypeDef(TypedDict):
    maxTokens: NotRequired[int]
    temperature: NotRequired[float]
    topP: NotRequired[float]
    stopSequences: NotRequired[Sequence[str]]


class PerformanceConfigurationTypeDef(TypedDict):
    latency: NotRequired[PerformanceConfigLatencyType]


class PromptVariableValuesTypeDef(TypedDict):
    text: NotRequired[str]


ServiceTierTypeDef = TypedDict(
    "ServiceTierTypeDef",
    {
        "type": ServiceTierTypeType,
    },
)


class TokenUsageTypeDef(TypedDict):
    inputTokens: int
    outputTokens: int
    totalTokens: int
    cacheReadInputTokens: NotRequired[int]
    cacheWriteInputTokens: NotRequired[int]


class ConverseStreamMetricsTypeDef(TypedDict):
    latencyMs: int


class InternalServerExceptionTypeDef(TypedDict):
    message: NotRequired[str]


class MessageStartEventTypeDef(TypedDict):
    role: ConversationRoleType


class MessageStopEventTypeDef(TypedDict):
    stopReason: StopReasonType
    additionalModelResponseFields: NotRequired[dict[str, Any]]


class ModelStreamErrorExceptionTypeDef(TypedDict):
    message: NotRequired[str]
    originalStatusCode: NotRequired[int]
    originalMessage: NotRequired[str]


class ServiceUnavailableExceptionTypeDef(TypedDict):
    message: NotRequired[str]


class ThrottlingExceptionTypeDef(TypedDict):
    message: NotRequired[str]


class ValidationExceptionTypeDef(TypedDict):
    message: NotRequired[str]


class GuardrailStreamConfigurationTypeDef(TypedDict):
    guardrailIdentifier: NotRequired[str]
    guardrailVersion: NotRequired[str]
    trace: NotRequired[GuardrailTraceType]
    streamProcessingMode: NotRequired[GuardrailStreamProcessingModeType]


class PromptRouterTraceTypeDef(TypedDict):
    invokedModelId: NotRequired[str]


class DocumentContentBlockTypeDef(TypedDict):
    text: NotRequired[str]


class GetAsyncInvokeRequestTypeDef(TypedDict):
    invocationArn: str


class GuardrailAutomatedReasoningRuleTypeDef(TypedDict):
    identifier: NotRequired[str]
    policyVersionArn: NotRequired[str]


class GuardrailAutomatedReasoningInputTextReferenceTypeDef(TypedDict):
    text: NotRequired[str]


class GuardrailAutomatedReasoningStatementTypeDef(TypedDict):
    logic: NotRequired[str]
    naturalLanguage: NotRequired[str]


class GuardrailTextBlockTypeDef(TypedDict):
    text: str
    qualifiers: NotRequired[Sequence[GuardrailContentQualifierType]]


GuardrailContentFilterTypeDef = TypedDict(
    "GuardrailContentFilterTypeDef",
    {
        "type": GuardrailContentFilterTypeType,
        "confidence": GuardrailContentFilterConfidenceType,
        "action": GuardrailContentPolicyActionType,
        "filterStrength": NotRequired[GuardrailContentFilterStrengthType],
        "detected": NotRequired[bool],
    },
)
GuardrailContextualGroundingFilterTypeDef = TypedDict(
    "GuardrailContextualGroundingFilterTypeDef",
    {
        "type": GuardrailContextualGroundingFilterTypeType,
        "threshold": float,
        "score": float,
        "action": GuardrailContextualGroundingPolicyActionType,
        "detected": NotRequired[bool],
    },
)


class GuardrailConverseTextBlockOutputTypeDef(TypedDict):
    text: str
    qualifiers: NotRequired[list[GuardrailConverseContentQualifierType]]


GuardrailConverseImageSourceOutputTypeDef = TypedDict(
    "GuardrailConverseImageSourceOutputTypeDef",
    {
        "bytes": NotRequired[bytes],
    },
)


class GuardrailConverseTextBlockTypeDef(TypedDict):
    text: str
    qualifiers: NotRequired[Sequence[GuardrailConverseContentQualifierType]]


class GuardrailImageCoverageTypeDef(TypedDict):
    guarded: NotRequired[int]
    total: NotRequired[int]


class GuardrailTextCharactersCoverageTypeDef(TypedDict):
    guarded: NotRequired[int]
    total: NotRequired[int]


class GuardrailCustomWordTypeDef(TypedDict):
    match: str
    action: GuardrailWordPolicyActionType
    detected: NotRequired[bool]


GuardrailManagedWordTypeDef = TypedDict(
    "GuardrailManagedWordTypeDef",
    {
        "match": str,
        "type": Literal["PROFANITY"],
        "action": GuardrailWordPolicyActionType,
        "detected": NotRequired[bool],
    },
)
GuardrailPiiEntityFilterTypeDef = TypedDict(
    "GuardrailPiiEntityFilterTypeDef",
    {
        "match": str,
        "type": GuardrailPiiEntityTypeType,
        "action": GuardrailSensitiveInformationPolicyActionType,
        "detected": NotRequired[bool],
    },
)


class GuardrailRegexFilterTypeDef(TypedDict):
    action: GuardrailSensitiveInformationPolicyActionType
    name: NotRequired[str]
    match: NotRequired[str]
    regex: NotRequired[str]
    detected: NotRequired[bool]


GuardrailTopicTypeDef = TypedDict(
    "GuardrailTopicTypeDef",
    {
        "name": str,
        "type": Literal["DENY"],
        "action": GuardrailTopicPolicyActionType,
        "detected": NotRequired[bool],
    },
)


class ModelTimeoutExceptionTypeDef(TypedDict):
    message: NotRequired[str]


class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]


TimestampTypeDef = Union[datetime, str]
PayloadPartTypeDef = TypedDict(
    "PayloadPartTypeDef",
    {
        "bytes": NotRequired[bytes],
    },
)


class ReasoningTextBlockTypeDef(TypedDict):
    text: str
    signature: NotRequired[str]


class SearchResultContentBlockTypeDef(TypedDict):
    text: str


class SpecificToolChoiceTypeDef(TypedDict):
    name: str


class TagTypeDef(TypedDict):
    key: str
    value: str


class SystemToolTypeDef(TypedDict):
    name: str


class ToolInputSchemaTypeDef(TypedDict):
    json: NotRequired[Mapping[str, Any]]


ToolUseBlockTypeDef = TypedDict(
    "ToolUseBlockTypeDef",
    {
        "toolUseId": str,
        "name": str,
        "input": Mapping[str, Any],
        "type": NotRequired[ToolUseTypeType],
    },
)


class CountTokensResponseTypeDef(TypedDict):
    inputTokens: int
    ResponseMetadata: ResponseMetadataTypeDef


class InvokeModelResponseTypeDef(TypedDict):
    body: StreamingBody
    contentType: str
    performanceConfigLatency: PerformanceConfigLatencyType
    serviceTier: ServiceTierTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class StartAsyncInvokeResponseTypeDef(TypedDict):
    invocationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class AsyncInvokeOutputDataConfigTypeDef(TypedDict):
    s3OutputDataConfig: NotRequired[AsyncInvokeS3OutputDataConfigTypeDef]


AudioSourceOutputTypeDef = TypedDict(
    "AudioSourceOutputTypeDef",
    {
        "bytes": NotRequired[bytes],
        "s3Location": NotRequired[S3LocationTypeDef],
    },
)
ImageSourceOutputTypeDef = TypedDict(
    "ImageSourceOutputTypeDef",
    {
        "bytes": NotRequired[bytes],
        "s3Location": NotRequired[S3LocationTypeDef],
    },
)
VideoSourceOutputTypeDef = TypedDict(
    "VideoSourceOutputTypeDef",
    {
        "bytes": NotRequired[bytes],
        "s3Location": NotRequired[S3LocationTypeDef],
    },
)
AudioSourceTypeDef = TypedDict(
    "AudioSourceTypeDef",
    {
        "bytes": NotRequired[BlobTypeDef],
        "s3Location": NotRequired[S3LocationTypeDef],
    },
)
BidirectionalInputPayloadPartTypeDef = TypedDict(
    "BidirectionalInputPayloadPartTypeDef",
    {
        "bytes": NotRequired[BlobTypeDef],
    },
)
GuardrailConverseImageSourceTypeDef = TypedDict(
    "GuardrailConverseImageSourceTypeDef",
    {
        "bytes": NotRequired[BlobTypeDef],
    },
)
GuardrailImageSourceTypeDef = TypedDict(
    "GuardrailImageSourceTypeDef",
    {
        "bytes": NotRequired[BlobTypeDef],
    },
)
ImageSourceTypeDef = TypedDict(
    "ImageSourceTypeDef",
    {
        "bytes": NotRequired[BlobTypeDef],
        "s3Location": NotRequired[S3LocationTypeDef],
    },
)


class InvokeModelRequestTypeDef(TypedDict):
    modelId: str
    body: NotRequired[BlobTypeDef]
    contentType: NotRequired[str]
    accept: NotRequired[str]
    trace: NotRequired[TraceType]
    guardrailIdentifier: NotRequired[str]
    guardrailVersion: NotRequired[str]
    performanceConfigLatency: NotRequired[PerformanceConfigLatencyType]
    serviceTier: NotRequired[ServiceTierTypeType]


class InvokeModelTokensRequestTypeDef(TypedDict):
    body: BlobTypeDef


class InvokeModelWithResponseStreamRequestTypeDef(TypedDict):
    modelId: str
    body: NotRequired[BlobTypeDef]
    contentType: NotRequired[str]
    accept: NotRequired[str]
    trace: NotRequired[TraceType]
    guardrailIdentifier: NotRequired[str]
    guardrailVersion: NotRequired[str]
    performanceConfigLatency: NotRequired[PerformanceConfigLatencyType]
    serviceTier: NotRequired[ServiceTierTypeType]


VideoSourceTypeDef = TypedDict(
    "VideoSourceTypeDef",
    {
        "bytes": NotRequired[BlobTypeDef],
        "s3Location": NotRequired[S3LocationTypeDef],
    },
)


class CitationLocationTypeDef(TypedDict):
    web: NotRequired[WebLocationTypeDef]
    documentChar: NotRequired[DocumentCharLocationTypeDef]
    documentPage: NotRequired[DocumentPageLocationTypeDef]
    documentChunk: NotRequired[DocumentChunkLocationTypeDef]
    searchResultLocation: NotRequired[SearchResultLocationTypeDef]


class ContentBlockStartTypeDef(TypedDict):
    toolUse: NotRequired[ToolUseBlockStartTypeDef]
    toolResult: NotRequired[ToolResultBlockStartTypeDef]
    image: NotRequired[ImageBlockStartTypeDef]


DocumentSourceOutputTypeDef = TypedDict(
    "DocumentSourceOutputTypeDef",
    {
        "bytes": NotRequired[bytes],
        "s3Location": NotRequired[S3LocationTypeDef],
        "text": NotRequired[str],
        "content": NotRequired[list[DocumentContentBlockTypeDef]],
    },
)
DocumentSourceTypeDef = TypedDict(
    "DocumentSourceTypeDef",
    {
        "bytes": NotRequired[BlobTypeDef],
        "s3Location": NotRequired[S3LocationTypeDef],
        "text": NotRequired[str],
        "content": NotRequired[Sequence[DocumentContentBlockTypeDef]],
    },
)
GuardrailAutomatedReasoningLogicWarningTypeDef = TypedDict(
    "GuardrailAutomatedReasoningLogicWarningTypeDef",
    {
        "type": NotRequired[GuardrailAutomatedReasoningLogicWarningTypeType],
        "premises": NotRequired[list[GuardrailAutomatedReasoningStatementTypeDef]],
        "claims": NotRequired[list[GuardrailAutomatedReasoningStatementTypeDef]],
    },
)


class GuardrailAutomatedReasoningScenarioTypeDef(TypedDict):
    statements: NotRequired[list[GuardrailAutomatedReasoningStatementTypeDef]]


class GuardrailAutomatedReasoningTranslationTypeDef(TypedDict):
    premises: NotRequired[list[GuardrailAutomatedReasoningStatementTypeDef]]
    claims: NotRequired[list[GuardrailAutomatedReasoningStatementTypeDef]]
    untranslatedPremises: NotRequired[list[GuardrailAutomatedReasoningInputTextReferenceTypeDef]]
    untranslatedClaims: NotRequired[list[GuardrailAutomatedReasoningInputTextReferenceTypeDef]]
    confidence: NotRequired[float]


class GuardrailContentPolicyAssessmentTypeDef(TypedDict):
    filters: list[GuardrailContentFilterTypeDef]


class GuardrailContextualGroundingPolicyAssessmentTypeDef(TypedDict):
    filters: NotRequired[list[GuardrailContextualGroundingFilterTypeDef]]


GuardrailConverseImageBlockOutputTypeDef = TypedDict(
    "GuardrailConverseImageBlockOutputTypeDef",
    {
        "format": GuardrailConverseImageFormatType,
        "source": GuardrailConverseImageSourceOutputTypeDef,
    },
)
GuardrailConverseTextBlockUnionTypeDef = Union[
    GuardrailConverseTextBlockTypeDef, GuardrailConverseTextBlockOutputTypeDef
]


class GuardrailCoverageTypeDef(TypedDict):
    textCharacters: NotRequired[GuardrailTextCharactersCoverageTypeDef]
    images: NotRequired[GuardrailImageCoverageTypeDef]


class GuardrailWordPolicyAssessmentTypeDef(TypedDict):
    customWords: list[GuardrailCustomWordTypeDef]
    managedWordLists: list[GuardrailManagedWordTypeDef]


class GuardrailSensitiveInformationPolicyAssessmentTypeDef(TypedDict):
    piiEntities: list[GuardrailPiiEntityFilterTypeDef]
    regexes: list[GuardrailRegexFilterTypeDef]


class GuardrailTopicPolicyAssessmentTypeDef(TypedDict):
    topics: list[GuardrailTopicTypeDef]


class InvokeModelWithBidirectionalStreamOutputTypeDef(TypedDict):
    chunk: NotRequired[BidirectionalOutputPayloadPartTypeDef]
    internalServerException: NotRequired[InternalServerExceptionTypeDef]
    modelStreamErrorException: NotRequired[ModelStreamErrorExceptionTypeDef]
    validationException: NotRequired[ValidationExceptionTypeDef]
    throttlingException: NotRequired[ThrottlingExceptionTypeDef]
    modelTimeoutException: NotRequired[ModelTimeoutExceptionTypeDef]
    serviceUnavailableException: NotRequired[ServiceUnavailableExceptionTypeDef]


class ListAsyncInvokesRequestPaginateTypeDef(TypedDict):
    submitTimeAfter: NotRequired[TimestampTypeDef]
    submitTimeBefore: NotRequired[TimestampTypeDef]
    statusEquals: NotRequired[AsyncInvokeStatusType]
    sortBy: NotRequired[Literal["SubmissionTime"]]
    sortOrder: NotRequired[SortOrderType]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]


class ListAsyncInvokesRequestTypeDef(TypedDict):
    submitTimeAfter: NotRequired[TimestampTypeDef]
    submitTimeBefore: NotRequired[TimestampTypeDef]
    statusEquals: NotRequired[AsyncInvokeStatusType]
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    sortBy: NotRequired[Literal["SubmissionTime"]]
    sortOrder: NotRequired[SortOrderType]


class ResponseStreamTypeDef(TypedDict):
    chunk: NotRequired[PayloadPartTypeDef]
    internalServerException: NotRequired[InternalServerExceptionTypeDef]
    modelStreamErrorException: NotRequired[ModelStreamErrorExceptionTypeDef]
    validationException: NotRequired[ValidationExceptionTypeDef]
    throttlingException: NotRequired[ThrottlingExceptionTypeDef]
    modelTimeoutException: NotRequired[ModelTimeoutExceptionTypeDef]
    serviceUnavailableException: NotRequired[ServiceUnavailableExceptionTypeDef]


class ReasoningContentBlockOutputTypeDef(TypedDict):
    reasoningText: NotRequired[ReasoningTextBlockTypeDef]
    redactedContent: NotRequired[bytes]


class ReasoningContentBlockTypeDef(TypedDict):
    reasoningText: NotRequired[ReasoningTextBlockTypeDef]
    redactedContent: NotRequired[BlobTypeDef]


class SearchResultBlockOutputTypeDef(TypedDict):
    source: str
    title: str
    content: list[SearchResultContentBlockTypeDef]
    citations: NotRequired[CitationsConfigTypeDef]


class SearchResultBlockTypeDef(TypedDict):
    source: str
    title: str
    content: Sequence[SearchResultContentBlockTypeDef]
    citations: NotRequired[CitationsConfigTypeDef]


ToolChoiceTypeDef = TypedDict(
    "ToolChoiceTypeDef",
    {
        "auto": NotRequired[Mapping[str, Any]],
        "any": NotRequired[Mapping[str, Any]],
        "tool": NotRequired[SpecificToolChoiceTypeDef],
    },
)


class ToolSpecificationTypeDef(TypedDict):
    name: str
    inputSchema: ToolInputSchemaTypeDef
    description: NotRequired[str]


ToolUseBlockUnionTypeDef = Union[ToolUseBlockTypeDef, ToolUseBlockOutputTypeDef]


class AsyncInvokeSummaryTypeDef(TypedDict):
    invocationArn: str
    modelArn: str
    submitTime: datetime
    outputDataConfig: AsyncInvokeOutputDataConfigTypeDef
    clientRequestToken: NotRequired[str]
    status: NotRequired[AsyncInvokeStatusType]
    failureMessage: NotRequired[str]
    lastModifiedTime: NotRequired[datetime]
    endTime: NotRequired[datetime]


class GetAsyncInvokeResponseTypeDef(TypedDict):
    invocationArn: str
    modelArn: str
    clientRequestToken: str
    status: AsyncInvokeStatusType
    failureMessage: str
    submitTime: datetime
    lastModifiedTime: datetime
    endTime: datetime
    outputDataConfig: AsyncInvokeOutputDataConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartAsyncInvokeRequestTypeDef(TypedDict):
    modelId: str
    modelInput: Mapping[str, Any]
    outputDataConfig: AsyncInvokeOutputDataConfigTypeDef
    clientRequestToken: NotRequired[str]
    tags: NotRequired[Sequence[TagTypeDef]]


AudioBlockOutputTypeDef = TypedDict(
    "AudioBlockOutputTypeDef",
    {
        "format": AudioFormatType,
        "source": AudioSourceOutputTypeDef,
        "error": NotRequired[ErrorBlockTypeDef],
    },
)


class ImageBlockDeltaTypeDef(TypedDict):
    source: NotRequired[ImageSourceOutputTypeDef]
    error: NotRequired[ErrorBlockTypeDef]


ImageBlockOutputTypeDef = TypedDict(
    "ImageBlockOutputTypeDef",
    {
        "format": ImageFormatType,
        "source": ImageSourceOutputTypeDef,
        "error": NotRequired[ErrorBlockTypeDef],
    },
)
VideoBlockOutputTypeDef = TypedDict(
    "VideoBlockOutputTypeDef",
    {
        "format": VideoFormatType,
        "source": VideoSourceOutputTypeDef,
    },
)
AudioSourceUnionTypeDef = Union[AudioSourceTypeDef, AudioSourceOutputTypeDef]


class InvokeModelWithBidirectionalStreamInputTypeDef(TypedDict):
    chunk: NotRequired[BidirectionalInputPayloadPartTypeDef]


GuardrailConverseImageSourceUnionTypeDef = Union[
    GuardrailConverseImageSourceTypeDef, GuardrailConverseImageSourceOutputTypeDef
]
GuardrailImageBlockTypeDef = TypedDict(
    "GuardrailImageBlockTypeDef",
    {
        "format": GuardrailImageFormatType,
        "source": GuardrailImageSourceTypeDef,
    },
)
ImageSourceUnionTypeDef = Union[ImageSourceTypeDef, ImageSourceOutputTypeDef]
VideoSourceUnionTypeDef = Union[VideoSourceTypeDef, VideoSourceOutputTypeDef]


class CitationOutputTypeDef(TypedDict):
    title: NotRequired[str]
    source: NotRequired[str]
    sourceContent: NotRequired[list[CitationSourceContentTypeDef]]
    location: NotRequired[CitationLocationTypeDef]


class CitationTypeDef(TypedDict):
    title: NotRequired[str]
    source: NotRequired[str]
    sourceContent: NotRequired[Sequence[CitationSourceContentTypeDef]]
    location: NotRequired[CitationLocationTypeDef]


class CitationsDeltaTypeDef(TypedDict):
    title: NotRequired[str]
    source: NotRequired[str]
    sourceContent: NotRequired[list[CitationSourceContentDeltaTypeDef]]
    location: NotRequired[CitationLocationTypeDef]


class ContentBlockStartEventTypeDef(TypedDict):
    start: ContentBlockStartTypeDef
    contentBlockIndex: int


DocumentBlockOutputTypeDef = TypedDict(
    "DocumentBlockOutputTypeDef",
    {
        "name": str,
        "source": DocumentSourceOutputTypeDef,
        "format": NotRequired[DocumentFormatType],
        "context": NotRequired[str],
        "citations": NotRequired[CitationsConfigTypeDef],
    },
)
DocumentSourceUnionTypeDef = Union[DocumentSourceTypeDef, DocumentSourceOutputTypeDef]


class GuardrailAutomatedReasoningImpossibleFindingTypeDef(TypedDict):
    translation: NotRequired[GuardrailAutomatedReasoningTranslationTypeDef]
    contradictingRules: NotRequired[list[GuardrailAutomatedReasoningRuleTypeDef]]
    logicWarning: NotRequired[GuardrailAutomatedReasoningLogicWarningTypeDef]


class GuardrailAutomatedReasoningInvalidFindingTypeDef(TypedDict):
    translation: NotRequired[GuardrailAutomatedReasoningTranslationTypeDef]
    contradictingRules: NotRequired[list[GuardrailAutomatedReasoningRuleTypeDef]]
    logicWarning: NotRequired[GuardrailAutomatedReasoningLogicWarningTypeDef]


class GuardrailAutomatedReasoningSatisfiableFindingTypeDef(TypedDict):
    translation: NotRequired[GuardrailAutomatedReasoningTranslationTypeDef]
    claimsTrueScenario: NotRequired[GuardrailAutomatedReasoningScenarioTypeDef]
    claimsFalseScenario: NotRequired[GuardrailAutomatedReasoningScenarioTypeDef]
    logicWarning: NotRequired[GuardrailAutomatedReasoningLogicWarningTypeDef]


class GuardrailAutomatedReasoningTranslationOptionTypeDef(TypedDict):
    translations: NotRequired[list[GuardrailAutomatedReasoningTranslationTypeDef]]


class GuardrailAutomatedReasoningValidFindingTypeDef(TypedDict):
    translation: NotRequired[GuardrailAutomatedReasoningTranslationTypeDef]
    claimsTrueScenario: NotRequired[GuardrailAutomatedReasoningScenarioTypeDef]
    supportingRules: NotRequired[list[GuardrailAutomatedReasoningRuleTypeDef]]
    logicWarning: NotRequired[GuardrailAutomatedReasoningLogicWarningTypeDef]


class GuardrailConverseContentBlockOutputTypeDef(TypedDict):
    text: NotRequired[GuardrailConverseTextBlockOutputTypeDef]
    image: NotRequired[GuardrailConverseImageBlockOutputTypeDef]


class GuardrailInvocationMetricsTypeDef(TypedDict):
    guardrailProcessingLatency: NotRequired[int]
    usage: NotRequired[GuardrailUsageTypeDef]
    guardrailCoverage: NotRequired[GuardrailCoverageTypeDef]


class InvokeModelWithBidirectionalStreamResponseTypeDef(TypedDict):
    body: EventStream[InvokeModelWithBidirectionalStreamOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class InvokeModelWithResponseStreamResponseTypeDef(TypedDict):
    body: EventStream[ResponseStreamTypeDef]
    contentType: str
    performanceConfigLatency: PerformanceConfigLatencyType
    serviceTier: ServiceTierTypeType
    ResponseMetadata: ResponseMetadataTypeDef


ReasoningContentBlockUnionTypeDef = Union[
    ReasoningContentBlockTypeDef, ReasoningContentBlockOutputTypeDef
]
SearchResultBlockUnionTypeDef = Union[SearchResultBlockTypeDef, SearchResultBlockOutputTypeDef]


class ToolTypeDef(TypedDict):
    toolSpec: NotRequired[ToolSpecificationTypeDef]
    systemTool: NotRequired[SystemToolTypeDef]
    cachePoint: NotRequired[CachePointBlockTypeDef]


class ListAsyncInvokesResponseTypeDef(TypedDict):
    asyncInvokeSummaries: list[AsyncInvokeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]


AudioBlockTypeDef = TypedDict(
    "AudioBlockTypeDef",
    {
        "format": AudioFormatType,
        "source": AudioSourceUnionTypeDef,
        "error": NotRequired[ErrorBlockTypeDef],
    },
)


class InvokeModelWithBidirectionalStreamRequestTypeDef(TypedDict):
    modelId: str
    body: EventStream[InvokeModelWithBidirectionalStreamInputTypeDef]


GuardrailConverseImageBlockTypeDef = TypedDict(
    "GuardrailConverseImageBlockTypeDef",
    {
        "format": GuardrailConverseImageFormatType,
        "source": GuardrailConverseImageSourceUnionTypeDef,
    },
)


class GuardrailContentBlockTypeDef(TypedDict):
    text: NotRequired[GuardrailTextBlockTypeDef]
    image: NotRequired[GuardrailImageBlockTypeDef]


ImageBlockTypeDef = TypedDict(
    "ImageBlockTypeDef",
    {
        "format": ImageFormatType,
        "source": ImageSourceUnionTypeDef,
        "error": NotRequired[ErrorBlockTypeDef],
    },
)
VideoBlockTypeDef = TypedDict(
    "VideoBlockTypeDef",
    {
        "format": VideoFormatType,
        "source": VideoSourceUnionTypeDef,
    },
)


class CitationsContentBlockOutputTypeDef(TypedDict):
    content: NotRequired[list[CitationGeneratedContentTypeDef]]
    citations: NotRequired[list[CitationOutputTypeDef]]


CitationUnionTypeDef = Union[CitationTypeDef, CitationOutputTypeDef]


class ContentBlockDeltaTypeDef(TypedDict):
    text: NotRequired[str]
    toolUse: NotRequired[ToolUseBlockDeltaTypeDef]
    toolResult: NotRequired[list[ToolResultBlockDeltaTypeDef]]
    reasoningContent: NotRequired[ReasoningContentBlockDeltaTypeDef]
    citation: NotRequired[CitationsDeltaTypeDef]
    image: NotRequired[ImageBlockDeltaTypeDef]


class ToolResultContentBlockOutputTypeDef(TypedDict):
    json: NotRequired[dict[str, Any]]
    text: NotRequired[str]
    image: NotRequired[ImageBlockOutputTypeDef]
    document: NotRequired[DocumentBlockOutputTypeDef]
    video: NotRequired[VideoBlockOutputTypeDef]
    searchResult: NotRequired[SearchResultBlockOutputTypeDef]


DocumentBlockTypeDef = TypedDict(
    "DocumentBlockTypeDef",
    {
        "name": str,
        "source": DocumentSourceUnionTypeDef,
        "format": NotRequired[DocumentFormatType],
        "context": NotRequired[str],
        "citations": NotRequired[CitationsConfigTypeDef],
    },
)


class GuardrailAutomatedReasoningTranslationAmbiguousFindingTypeDef(TypedDict):
    options: NotRequired[list[GuardrailAutomatedReasoningTranslationOptionTypeDef]]
    differenceScenarios: NotRequired[list[GuardrailAutomatedReasoningScenarioTypeDef]]


class ToolConfigurationTypeDef(TypedDict):
    tools: Sequence[ToolTypeDef]
    toolChoice: NotRequired[ToolChoiceTypeDef]


AudioBlockUnionTypeDef = Union[AudioBlockTypeDef, AudioBlockOutputTypeDef]
GuardrailConverseImageBlockUnionTypeDef = Union[
    GuardrailConverseImageBlockTypeDef, GuardrailConverseImageBlockOutputTypeDef
]


class ApplyGuardrailRequestTypeDef(TypedDict):
    guardrailIdentifier: str
    guardrailVersion: str
    source: GuardrailContentSourceType
    content: Sequence[GuardrailContentBlockTypeDef]
    outputScope: NotRequired[GuardrailOutputScopeType]


ImageBlockUnionTypeDef = Union[ImageBlockTypeDef, ImageBlockOutputTypeDef]
VideoBlockUnionTypeDef = Union[VideoBlockTypeDef, VideoBlockOutputTypeDef]


class CitationsContentBlockTypeDef(TypedDict):
    content: NotRequired[Sequence[CitationGeneratedContentTypeDef]]
    citations: NotRequired[Sequence[CitationUnionTypeDef]]


class ContentBlockDeltaEventTypeDef(TypedDict):
    delta: ContentBlockDeltaTypeDef
    contentBlockIndex: int


ToolResultBlockOutputTypeDef = TypedDict(
    "ToolResultBlockOutputTypeDef",
    {
        "toolUseId": str,
        "content": list[ToolResultContentBlockOutputTypeDef],
        "status": NotRequired[ToolResultStatusType],
        "type": NotRequired[str],
    },
)
DocumentBlockUnionTypeDef = Union[DocumentBlockTypeDef, DocumentBlockOutputTypeDef]


class GuardrailAutomatedReasoningFindingTypeDef(TypedDict):
    valid: NotRequired[GuardrailAutomatedReasoningValidFindingTypeDef]
    invalid: NotRequired[GuardrailAutomatedReasoningInvalidFindingTypeDef]
    satisfiable: NotRequired[GuardrailAutomatedReasoningSatisfiableFindingTypeDef]
    impossible: NotRequired[GuardrailAutomatedReasoningImpossibleFindingTypeDef]
    translationAmbiguous: NotRequired[GuardrailAutomatedReasoningTranslationAmbiguousFindingTypeDef]
    tooComplex: NotRequired[dict[str, Any]]
    noTranslations: NotRequired[dict[str, Any]]


class GuardrailConverseContentBlockTypeDef(TypedDict):
    text: NotRequired[GuardrailConverseTextBlockUnionTypeDef]
    image: NotRequired[GuardrailConverseImageBlockUnionTypeDef]


CitationsContentBlockUnionTypeDef = Union[
    CitationsContentBlockTypeDef, CitationsContentBlockOutputTypeDef
]


class ContentBlockOutputTypeDef(TypedDict):
    text: NotRequired[str]
    image: NotRequired[ImageBlockOutputTypeDef]
    document: NotRequired[DocumentBlockOutputTypeDef]
    video: NotRequired[VideoBlockOutputTypeDef]
    audio: NotRequired[AudioBlockOutputTypeDef]
    toolUse: NotRequired[ToolUseBlockOutputTypeDef]
    toolResult: NotRequired[ToolResultBlockOutputTypeDef]
    guardContent: NotRequired[GuardrailConverseContentBlockOutputTypeDef]
    cachePoint: NotRequired[CachePointBlockTypeDef]
    reasoningContent: NotRequired[ReasoningContentBlockOutputTypeDef]
    citationsContent: NotRequired[CitationsContentBlockOutputTypeDef]
    searchResult: NotRequired[SearchResultBlockOutputTypeDef]


class ToolResultContentBlockTypeDef(TypedDict):
    json: NotRequired[Mapping[str, Any]]
    text: NotRequired[str]
    image: NotRequired[ImageBlockUnionTypeDef]
    document: NotRequired[DocumentBlockUnionTypeDef]
    video: NotRequired[VideoBlockUnionTypeDef]
    searchResult: NotRequired[SearchResultBlockUnionTypeDef]


class GuardrailAutomatedReasoningPolicyAssessmentTypeDef(TypedDict):
    findings: NotRequired[list[GuardrailAutomatedReasoningFindingTypeDef]]


GuardrailConverseContentBlockUnionTypeDef = Union[
    GuardrailConverseContentBlockTypeDef, GuardrailConverseContentBlockOutputTypeDef
]


class MessageOutputTypeDef(TypedDict):
    role: ConversationRoleType
    content: list[ContentBlockOutputTypeDef]


ToolResultContentBlockUnionTypeDef = Union[
    ToolResultContentBlockTypeDef, ToolResultContentBlockOutputTypeDef
]


class GuardrailAssessmentTypeDef(TypedDict):
    topicPolicy: NotRequired[GuardrailTopicPolicyAssessmentTypeDef]
    contentPolicy: NotRequired[GuardrailContentPolicyAssessmentTypeDef]
    wordPolicy: NotRequired[GuardrailWordPolicyAssessmentTypeDef]
    sensitiveInformationPolicy: NotRequired[GuardrailSensitiveInformationPolicyAssessmentTypeDef]
    contextualGroundingPolicy: NotRequired[GuardrailContextualGroundingPolicyAssessmentTypeDef]
    automatedReasoningPolicy: NotRequired[GuardrailAutomatedReasoningPolicyAssessmentTypeDef]
    invocationMetrics: NotRequired[GuardrailInvocationMetricsTypeDef]
    appliedGuardrailDetails: NotRequired[AppliedGuardrailDetailsTypeDef]


class SystemContentBlockTypeDef(TypedDict):
    text: NotRequired[str]
    guardContent: NotRequired[GuardrailConverseContentBlockUnionTypeDef]
    cachePoint: NotRequired[CachePointBlockTypeDef]


class ConverseOutputTypeDef(TypedDict):
    message: NotRequired[MessageOutputTypeDef]


ToolResultBlockTypeDef = TypedDict(
    "ToolResultBlockTypeDef",
    {
        "toolUseId": str,
        "content": Sequence[ToolResultContentBlockUnionTypeDef],
        "status": NotRequired[ToolResultStatusType],
        "type": NotRequired[str],
    },
)


class ApplyGuardrailResponseTypeDef(TypedDict):
    usage: GuardrailUsageTypeDef
    action: GuardrailActionType
    actionReason: str
    outputs: list[GuardrailOutputContentTypeDef]
    assessments: list[GuardrailAssessmentTypeDef]
    guardrailCoverage: GuardrailCoverageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GuardrailTraceAssessmentTypeDef(TypedDict):
    modelOutput: NotRequired[list[str]]
    inputAssessment: NotRequired[dict[str, GuardrailAssessmentTypeDef]]
    outputAssessments: NotRequired[dict[str, list[GuardrailAssessmentTypeDef]]]
    actionReason: NotRequired[str]


ToolResultBlockUnionTypeDef = Union[ToolResultBlockTypeDef, ToolResultBlockOutputTypeDef]


class ConverseStreamTraceTypeDef(TypedDict):
    guardrail: NotRequired[GuardrailTraceAssessmentTypeDef]
    promptRouter: NotRequired[PromptRouterTraceTypeDef]


class ConverseTraceTypeDef(TypedDict):
    guardrail: NotRequired[GuardrailTraceAssessmentTypeDef]
    promptRouter: NotRequired[PromptRouterTraceTypeDef]


class ContentBlockTypeDef(TypedDict):
    text: NotRequired[str]
    image: NotRequired[ImageBlockUnionTypeDef]
    document: NotRequired[DocumentBlockUnionTypeDef]
    video: NotRequired[VideoBlockUnionTypeDef]
    audio: NotRequired[AudioBlockUnionTypeDef]
    toolUse: NotRequired[ToolUseBlockUnionTypeDef]
    toolResult: NotRequired[ToolResultBlockUnionTypeDef]
    guardContent: NotRequired[GuardrailConverseContentBlockUnionTypeDef]
    cachePoint: NotRequired[CachePointBlockTypeDef]
    reasoningContent: NotRequired[ReasoningContentBlockUnionTypeDef]
    citationsContent: NotRequired[CitationsContentBlockUnionTypeDef]
    searchResult: NotRequired[SearchResultBlockUnionTypeDef]


class ConverseStreamMetadataEventTypeDef(TypedDict):
    usage: TokenUsageTypeDef
    metrics: ConverseStreamMetricsTypeDef
    trace: NotRequired[ConverseStreamTraceTypeDef]
    performanceConfig: NotRequired[PerformanceConfigurationTypeDef]
    serviceTier: NotRequired[ServiceTierTypeDef]


class ConverseResponseTypeDef(TypedDict):
    output: ConverseOutputTypeDef
    stopReason: StopReasonType
    usage: TokenUsageTypeDef
    metrics: ConverseMetricsTypeDef
    additionalModelResponseFields: dict[str, Any]
    trace: ConverseTraceTypeDef
    performanceConfig: PerformanceConfigurationTypeDef
    serviceTier: ServiceTierTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


ContentBlockUnionTypeDef = Union[ContentBlockTypeDef, ContentBlockOutputTypeDef]


class ConverseStreamOutputTypeDef(TypedDict):
    messageStart: NotRequired[MessageStartEventTypeDef]
    contentBlockStart: NotRequired[ContentBlockStartEventTypeDef]
    contentBlockDelta: NotRequired[ContentBlockDeltaEventTypeDef]
    contentBlockStop: NotRequired[ContentBlockStopEventTypeDef]
    messageStop: NotRequired[MessageStopEventTypeDef]
    metadata: NotRequired[ConverseStreamMetadataEventTypeDef]
    internalServerException: NotRequired[InternalServerExceptionTypeDef]
    modelStreamErrorException: NotRequired[ModelStreamErrorExceptionTypeDef]
    validationException: NotRequired[ValidationExceptionTypeDef]
    throttlingException: NotRequired[ThrottlingExceptionTypeDef]
    serviceUnavailableException: NotRequired[ServiceUnavailableExceptionTypeDef]


class MessageTypeDef(TypedDict):
    role: ConversationRoleType
    content: Sequence[ContentBlockUnionTypeDef]


class ConverseStreamResponseTypeDef(TypedDict):
    stream: EventStream[ConverseStreamOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


MessageUnionTypeDef = Union[MessageTypeDef, MessageOutputTypeDef]


class ConverseRequestTypeDef(TypedDict):
    modelId: str
    messages: NotRequired[Sequence[MessageUnionTypeDef]]
    system: NotRequired[Sequence[SystemContentBlockTypeDef]]
    inferenceConfig: NotRequired[InferenceConfigurationTypeDef]
    toolConfig: NotRequired[ToolConfigurationTypeDef]
    guardrailConfig: NotRequired[GuardrailConfigurationTypeDef]
    additionalModelRequestFields: NotRequired[Mapping[str, Any]]
    promptVariables: NotRequired[Mapping[str, PromptVariableValuesTypeDef]]
    additionalModelResponseFieldPaths: NotRequired[Sequence[str]]
    requestMetadata: NotRequired[Mapping[str, str]]
    performanceConfig: NotRequired[PerformanceConfigurationTypeDef]
    serviceTier: NotRequired[ServiceTierTypeDef]


class ConverseStreamRequestTypeDef(TypedDict):
    modelId: str
    messages: NotRequired[Sequence[MessageUnionTypeDef]]
    system: NotRequired[Sequence[SystemContentBlockTypeDef]]
    inferenceConfig: NotRequired[InferenceConfigurationTypeDef]
    toolConfig: NotRequired[ToolConfigurationTypeDef]
    guardrailConfig: NotRequired[GuardrailStreamConfigurationTypeDef]
    additionalModelRequestFields: NotRequired[Mapping[str, Any]]
    promptVariables: NotRequired[Mapping[str, PromptVariableValuesTypeDef]]
    additionalModelResponseFieldPaths: NotRequired[Sequence[str]]
    requestMetadata: NotRequired[Mapping[str, str]]
    performanceConfig: NotRequired[PerformanceConfigurationTypeDef]
    serviceTier: NotRequired[ServiceTierTypeDef]


class ConverseTokensRequestTypeDef(TypedDict):
    messages: NotRequired[Sequence[MessageUnionTypeDef]]
    system: NotRequired[Sequence[SystemContentBlockTypeDef]]
    toolConfig: NotRequired[ToolConfigurationTypeDef]
    additionalModelRequestFields: NotRequired[Mapping[str, Any]]


class CountTokensInputTypeDef(TypedDict):
    invokeModel: NotRequired[InvokeModelTokensRequestTypeDef]
    converse: NotRequired[ConverseTokensRequestTypeDef]


CountTokensRequestTypeDef = TypedDict(
    "CountTokensRequestTypeDef",
    {
        "modelId": str,
        "input": CountTokensInputTypeDef,
    },
)

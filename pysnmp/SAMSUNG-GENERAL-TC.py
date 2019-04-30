#
# PySNMP MIB module SAMSUNG-GENERAL-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SAMSUNG-GENERAL-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:52:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
samsungCommonMIB, = mibBuilder.importSymbols("SAMSUNG-COMMON-MIB", "samsungCommonMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Bits, Counter32, Counter64, ObjectIdentity, MibIdentifier, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, ModuleIdentity, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "Counter32", "Counter64", "ObjectIdentity", "MibIdentifier", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "ModuleIdentity", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
scmGeneralTC = ModuleIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50))
if mibBuilder.loadTexts: scmGeneralTC.setLastUpdated('0407170000Z')
if mibBuilder.loadTexts: scmGeneralTC.setOrganization('Samsung Corporation - SCMI Working Group')
class Cardinal16(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 32767)

class Cardinal32(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Cardinal64High(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Cardinal64Low(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class CodedCountry(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2)

class CodedLanguage(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2)

class CodeIndexedStringIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Counter64High(TextualConvention, Counter32):
    status = 'current'

class Counter64Low(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Gauge64High(TextualConvention, Gauge32):
    status = 'current'

class Gauge64Low(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Integer64High(TextualConvention, Integer32):
    status = 'current'

class Integer64Low(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Ordinal16(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 32767)

class Ordinal32(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class Ordinal64High(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class Ordinal64Low(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

zeroDotZero = MibIdentifier((0, 0))
scmGenZeroDotZero = ObjectIdentity((0, 0, 0))
if mibBuilder.loadTexts: scmGenZeroDotZero.setStatus('current')
class ScmFixedLocaleDisplayString(TextualConvention, OctetString):
    reference = " See: 'ScmFixedLocaleUtf8String' in this module. See: 'ScmNamedLocaleUtf8String' in this module. See: 'InternationalDisplayString' in IETF Host Resources MIB (RFC 2790), 'DisplayString' in IETF SNMPv2 TC (RFC 1903/2579), 'CodeIndexedStringIndex' in this module, and 'OCTET STRING' in OSI ASN.1 (CCITT X.208/X.209 | ISO 8824/8825)."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class ScmFixedLocaleUtf8String(TextualConvention, OctetString):
    reference = " See: 'UTF-8, a transformation of ISO 10646' (RFC 2279) and 'IETF Policy on Character Sets and Languages' (RFC 2277). See: 'ScmFixedLocaleDisplayString' in this module. See: 'ScmNamedLocaleUtf8String' in this module. See: 'InternationalDisplayString' in IETF Host Resources MIB (RFC 2790), 'DisplayString' in IETF SNMPv2 TC (RFC 1903/2579), 'CodeIndexedStringIndex' in this module, and 'OCTET STRING' in OSI ASN.1 (CCITT X.208/X.209 | ISO 8824/8825)."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class ScmNamedLocaleUtf8String(TextualConvention, OctetString):
    reference = " See: 'UTF-8, a transformation of ISO 10646' (RFC 2279) and 'IETF Policy on Character Sets and Languages' (RFC 2277). See: 'ScmFixedLocaleDisplayString' in this module. See: 'ScmFixedLocaleUtf8String' in this module. See: 'InternationalDisplayString' in IETF Host Resources MIB (RFC 2790), 'DisplayString' in IETF SNMPv2 TC (RFC 1903/2579), 'CodeIndexedStringIndex' in this module, and 'OCTET STRING' in OSI ASN.1 (CCITT X.208/X.209 | ISO 8824/8825)."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class ScmGenGroupSupport(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmGenLogFullPolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("disableService", 3), ("disableAndPauseService", 4), ("enableServiceAndFlushLog", 5), ("enableServiceAndFlushOldest", 6))

class ScmGenMessageMapStringLabel(TextualConvention, OctetString):
    reference = " See: 'scmGenMessageMapStringLabel' in SCMI General MIB. See: 'deviceLifetimeUsage', 'deviceAccountingUsage', 'deviceLifetimeErrorCount', and 'deviceLifetimeWarningCount' in 'ScmHrDevDetailType' textual convention in SCMI Host Resources Ext TC."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class ScmGenNotifyDetailType(TextualConvention, Integer32):
    reference = " See: Section 5 'Subscription Object' and Section 5.3 'Subscription Template Attributes' and section 5.4 'Subscription Description Attributes' in IPP Notify (draft-ietf-ipp-not-spec-06.txt). See: Section 5 'Service Attributes' (encoding rules) in Service Location Protocol v2 (RFC 2608)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 10, 20, 21, 22, 23, 30, 31, 32, 33))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("notifyRecipientURI", 10), ("notifyEventNames", 20), ("notifyEventDelay", 21), ("notifySeverityFilter", 22), ("notifyTrainingFilter", 23), ("notifyMessageHeaderKeys", 30), ("notifyMessageHeaderText", 31), ("notifyMessageContentKeys", 32), ("notifyMessageContentText", 33))

class ScmGenNotifySchemeSupport(TextualConvention, Integer32):
    reference = " See: 'scmGenBaseNotifySchemeSupport' and 'scmGenBaseSNMPDomainSupport' in SCMI General MIB. See: Cited IETF URI/URL specifications."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmGenNotifySeverityFilter(TextualConvention, Integer32):
    reference = " See: 'prtAlertSeverityLevel' in IETF Printer MIB (RFC 1759). See: 'scmGenBaseNotifySeveritySupport' and 'scmGenTrapViewNotifySeverity' in SCMI General MIB."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmGenNotifyTrainingFilter(TextualConvention, Integer32):
    reference = " See: 'prtAlertTrainingLevel' in IETF Printer MIB (RFC 1759). See: 'scmGenBaseNotifyTrainingSupport' and 'scmGenTrapViewNotifyTraining' in SCMI General MIB."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class ScmGenOptionValueSyntax(TextualConvention, Integer32):
    reference = " See: 'scmGenOptionTable' in SCMI General MIB See: 'scmCommsOptionTable' in SCMI Comms Config MIB See: 'scmHrDevDetailTable' in SCMI Host Resources Ext MIB See: 'scmHrStorageDetailTable' in SCMI Host Resources Ext MIB See: 'scmSvcMonServiceDetailTable' in SCMI Service Mon MIB See: 'scmSecProfileDetailTable' in SCMI Security MIB"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("integerNumber", 3), ("integerCounter", 4), ("integerEnum", 5), ("integerGauge", 6), ("integerIndex", 7), ("integerTruthValue", 8), ("oidObject", 9), ("oidAutonomous", 10), ("stringBinary", 11), ("stringDisplay", 12), ("stringLocalization", 13), ("stringCodedCharSet", 14), ("stringDynamicLocalization", 15), ("stringUtf8Localization", 16))

class ScmGenReconfOptionState(TextualConvention, Integer32):
    reference = " See: 'scmGenReconfError[Index|Status]'"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("idle", 1), ("validateForImmediateChange", 2), ("validateForRebootChange", 3), ("validateForImmediateReboot", 4), ("validateInProgress", 5), ("activateForImmediateChange", 6), ("activateForRebootChange", 7), ("activateForImmediateReboot", 8), ("activateInProgress", 9))

class ScmGenRowPersistence(TextualConvention, Integer32):
    reference = " See: 'hrStorageType' in the Storage group of the IETF Host Resources MIB (RFC 2790). See: 'StorageType' textual convention in the Historic SNMPv2 Party MIB (RFC 1447). See: 'StorageType' textual convention in the IETF SNMPv2 Textual Conventions (RFC 2579)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("unknown", 2), ("volatile", 3), ("nonvolatile", 4), ("permanent", 5), ("readonly", 6))

class ScmGenSNMPDomain(TextualConvention, Integer32):
    reference = " See: 'scmGenBaseSNMPDomainSupport' and 'scmGenTrapClientSNMPDomain' in SCMI General MIB. See: Cited IETF SNMP specifications."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 10, 11, 20, 30))
    namedValues = NamedValues(("snmpUDPDomain", 1), ("snmpCLNSDomain", 2), ("snmpCONSDomain", 3), ("snmpDDPDomain", 4), ("snmpIPXDomain", 5), ("snmpNetBIOSDomain", 10), ("snmpNetBEUIDomain", 11), ("snmpTCPDomain", 20), ("uriNotifyDomain", 30))

class ScmGenSNMPVersion(TextualConvention, Integer32):
    reference = " See: 'scmGenBaseSNMPVersionSupport' and 'scmGenTrapClientSNMPVersion' in SCMI General MIB. See: Cited IETF SNMP specifications."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("unknown", 1), ("other", 2), ("snmpV1Community", 3), ("snmpV1Party", 4), ("snmpV2Party", 5), ("snmpV2Community", 6), ("snmpV2Usec", 7), ("snmpV2Star", 8), ("snmpV2Secure", 9), ("snmpV3Secure", 10))

class ScmGenSNMPv2ErrorStatus(TextualConvention, Integer32):
    reference = " See: 'error-status' in SNMPv2 Protocol (RFC 1448/1905)"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18))
    namedValues = NamedValues(("noError", 0), ("tooBig", 1), ("noSuchName", 2), ("badValue", 3), ("readOnly", 4), ("genErr", 5), ("noAccess", 6), ("wrongType", 7), ("wrongLength", 8), ("wrongEncoding", 9), ("wrongValue", 10), ("noCreation", 11), ("inconsistentValue", 12), ("resourceUnavailable", 13), ("commitFailed", 14), ("undoFailed", 15), ("authorizationError", 16), ("notWritable", 17), ("inconsistentName", 18))

class ScmGlobalUniqueID(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

sCmGeneralDummy = MibIdentifier((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999))
sCmGenCardinal16 = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 1), Cardinal16())
if mibBuilder.loadTexts: sCmGenCardinal16.setStatus('current')
sCmGenCardinal32 = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 2), Cardinal32())
if mibBuilder.loadTexts: sCmGenCardinal32.setStatus('current')
sCmGenCardinal64High = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 3), Cardinal64High())
if mibBuilder.loadTexts: sCmGenCardinal64High.setStatus('current')
sCmGenCardinal64Low = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 4), Cardinal64Low())
if mibBuilder.loadTexts: sCmGenCardinal64Low.setStatus('current')
sCmGenCodedCountry = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 5), CodedCountry())
if mibBuilder.loadTexts: sCmGenCodedCountry.setStatus('current')
sCmGenCodedLanguage = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 6), CodedLanguage())
if mibBuilder.loadTexts: sCmGenCodedLanguage.setStatus('current')
sCmGenCodeIndexedStringIndex = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 7), CodeIndexedStringIndex())
if mibBuilder.loadTexts: sCmGenCodeIndexedStringIndex.setStatus('current')
sCmGenCounter64High = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 8), Counter64High())
if mibBuilder.loadTexts: sCmGenCounter64High.setStatus('current')
sCmGenCounter64Low = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 9), Counter64Low())
if mibBuilder.loadTexts: sCmGenCounter64Low.setStatus('current')
sCmGenGauge64High = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 10), Gauge64High())
if mibBuilder.loadTexts: sCmGenGauge64High.setStatus('current')
sCmGenGauge64Low = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 11), Gauge64Low())
if mibBuilder.loadTexts: sCmGenGauge64Low.setStatus('current')
sCmGenInteger64High = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 12), Integer64High())
if mibBuilder.loadTexts: sCmGenInteger64High.setStatus('current')
sCmGenInteger64Low = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 13), Integer64Low())
if mibBuilder.loadTexts: sCmGenInteger64Low.setStatus('current')
sCmGenOrdinal16 = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 14), Ordinal16())
if mibBuilder.loadTexts: sCmGenOrdinal16.setStatus('current')
sCmGenOrdinal32 = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 15), Ordinal32())
if mibBuilder.loadTexts: sCmGenOrdinal32.setStatus('current')
sCmGenOrdinal64High = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 16), Ordinal64High())
if mibBuilder.loadTexts: sCmGenOrdinal64High.setStatus('current')
sCmGenOrdinal64Low = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 17), Ordinal64Low())
if mibBuilder.loadTexts: sCmGenOrdinal64Low.setStatus('current')
sCmGenFixedLocaleDisplayString = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 18), ScmFixedLocaleDisplayString())
if mibBuilder.loadTexts: sCmGenFixedLocaleDisplayString.setStatus('current')
sCmGenGroupSupport = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 19), ScmGenGroupSupport())
if mibBuilder.loadTexts: sCmGenGroupSupport.setStatus('current')
sCmGenLogFullPolicy = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 20), ScmGenLogFullPolicy())
if mibBuilder.loadTexts: sCmGenLogFullPolicy.setStatus('current')
sCmGenOptionValueSyntax = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 21), ScmGenOptionValueSyntax())
if mibBuilder.loadTexts: sCmGenOptionValueSyntax.setStatus('current')
sCmGenReconfOptionState = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 22), ScmGenReconfOptionState())
if mibBuilder.loadTexts: sCmGenReconfOptionState.setStatus('current')
sCmGenRowPersistence = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 23), ScmGenRowPersistence())
if mibBuilder.loadTexts: sCmGenRowPersistence.setStatus('current')
sCmGenSNMPDomain = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 24), ScmGenSNMPDomain())
if mibBuilder.loadTexts: sCmGenSNMPDomain.setStatus('current')
sCmGenSNMPVersion = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 25), ScmGenSNMPVersion())
if mibBuilder.loadTexts: sCmGenSNMPVersion.setStatus('current')
sCmGenSNMPv2ErrorStatus = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 26), ScmGenSNMPv2ErrorStatus())
if mibBuilder.loadTexts: sCmGenSNMPv2ErrorStatus.setStatus('current')
sCmGenGlobalUniqueID = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 27), ScmGlobalUniqueID())
if mibBuilder.loadTexts: sCmGenGlobalUniqueID.setStatus('current')
sCmGenFixedLocaleUtf8String = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 28), ScmFixedLocaleUtf8String())
if mibBuilder.loadTexts: sCmGenFixedLocaleUtf8String.setStatus('current')
sCmGenMessageMapStringLabel = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 29), ScmGenMessageMapStringLabel())
if mibBuilder.loadTexts: sCmGenMessageMapStringLabel.setStatus('current')
sCmGenNamedLocaleUtf8String = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 30), ScmNamedLocaleUtf8String())
if mibBuilder.loadTexts: sCmGenNamedLocaleUtf8String.setStatus('current')
sCmGenNotifySchemeSupport = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 31), ScmGenNotifySchemeSupport())
if mibBuilder.loadTexts: sCmGenNotifySchemeSupport.setStatus('current')
sCmGenNotifySeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 32), ScmGenNotifySeverityFilter())
if mibBuilder.loadTexts: sCmGenNotifySeverityFilter.setStatus('current')
sCmGenNotifyTrainingFilter = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 33), ScmGenNotifyTrainingFilter())
if mibBuilder.loadTexts: sCmGenNotifyTrainingFilter.setStatus('current')
sCmGenNotifyDetailType = MibScalar((1, 3, 6, 1, 4, 1, 236, 11, 5, 11, 50, 999, 34), ScmGenNotifyDetailType())
if mibBuilder.loadTexts: sCmGenNotifyDetailType.setStatus('current')
mibBuilder.exportSymbols("SAMSUNG-GENERAL-TC", CodedCountry=CodedCountry, ScmGenRowPersistence=ScmGenRowPersistence, ScmGenSNMPv2ErrorStatus=ScmGenSNMPv2ErrorStatus, ScmGenReconfOptionState=ScmGenReconfOptionState, ScmFixedLocaleUtf8String=ScmFixedLocaleUtf8String, ScmNamedLocaleUtf8String=ScmNamedLocaleUtf8String, ScmGenNotifyDetailType=ScmGenNotifyDetailType, sCmGenOrdinal64High=sCmGenOrdinal64High, Counter64High=Counter64High, ScmGenNotifySchemeSupport=ScmGenNotifySchemeSupport, sCmGenCardinal64High=sCmGenCardinal64High, sCmGenOptionValueSyntax=sCmGenOptionValueSyntax, sCmGenRowPersistence=sCmGenRowPersistence, sCmGenNamedLocaleUtf8String=sCmGenNamedLocaleUtf8String, sCmGenOrdinal16=sCmGenOrdinal16, sCmGenCodeIndexedStringIndex=sCmGenCodeIndexedStringIndex, Cardinal64High=Cardinal64High, sCmGenNotifySchemeSupport=sCmGenNotifySchemeSupport, ScmGenSNMPDomain=ScmGenSNMPDomain, sCmGeneralDummy=sCmGeneralDummy, sCmGenSNMPv2ErrorStatus=sCmGenSNMPv2ErrorStatus, zeroDotZero=zeroDotZero, sCmGenInteger64High=sCmGenInteger64High, sCmGenLogFullPolicy=sCmGenLogFullPolicy, sCmGenNotifyDetailType=sCmGenNotifyDetailType, sCmGenNotifyTrainingFilter=sCmGenNotifyTrainingFilter, sCmGenGroupSupport=sCmGenGroupSupport, sCmGenCardinal64Low=sCmGenCardinal64Low, Cardinal16=Cardinal16, ScmGenGroupSupport=ScmGenGroupSupport, Ordinal16=Ordinal16, sCmGenCardinal16=sCmGenCardinal16, Counter64Low=Counter64Low, sCmGenCounter64High=sCmGenCounter64High, Ordinal64Low=Ordinal64Low, ScmGlobalUniqueID=ScmGlobalUniqueID, Integer64High=Integer64High, Cardinal32=Cardinal32, sCmGenGauge64Low=sCmGenGauge64Low, sCmGenOrdinal64Low=sCmGenOrdinal64Low, sCmGenInteger64Low=sCmGenInteger64Low, ScmGenMessageMapStringLabel=ScmGenMessageMapStringLabel, sCmGenSNMPDomain=sCmGenSNMPDomain, CodeIndexedStringIndex=CodeIndexedStringIndex, sCmGenMessageMapStringLabel=sCmGenMessageMapStringLabel, ScmGenNotifySeverityFilter=ScmGenNotifySeverityFilter, PYSNMP_MODULE_ID=scmGeneralTC, sCmGenOrdinal32=sCmGenOrdinal32, sCmGenCodedCountry=sCmGenCodedCountry, scmGeneralTC=scmGeneralTC, CodedLanguage=CodedLanguage, sCmGenReconfOptionState=sCmGenReconfOptionState, sCmGenFixedLocaleUtf8String=sCmGenFixedLocaleUtf8String, sCmGenCodedLanguage=sCmGenCodedLanguage, Integer64Low=Integer64Low, sCmGenGauge64High=sCmGenGauge64High, ScmGenLogFullPolicy=ScmGenLogFullPolicy, sCmGenGlobalUniqueID=sCmGenGlobalUniqueID, Gauge64Low=Gauge64Low, scmGenZeroDotZero=scmGenZeroDotZero, Ordinal64High=Ordinal64High, ScmFixedLocaleDisplayString=ScmFixedLocaleDisplayString, Gauge64High=Gauge64High, sCmGenCardinal32=sCmGenCardinal32, Cardinal64Low=Cardinal64Low, ScmGenOptionValueSyntax=ScmGenOptionValueSyntax, sCmGenNotifySeverityFilter=sCmGenNotifySeverityFilter, Ordinal32=Ordinal32, sCmGenSNMPVersion=sCmGenSNMPVersion, sCmGenFixedLocaleDisplayString=sCmGenFixedLocaleDisplayString, ScmGenNotifyTrainingFilter=ScmGenNotifyTrainingFilter, sCmGenCounter64Low=sCmGenCounter64Low, ScmGenSNMPVersion=ScmGenSNMPVersion)

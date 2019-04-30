#
# PySNMP MIB module BTI7800-CONDITIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BTI7800-CONDITIONS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, enterprises, Unsigned32, ModuleIdentity, ObjectIdentity, Counter32, NotificationType, Integer32, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "enterprises", "Unsigned32", "ModuleIdentity", "ObjectIdentity", "Counter32", "NotificationType", "Integer32", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "TimeTicks")
TextualConvention, RowStatus, DisplayString, TruthValue, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue", "DateAndTime")
bTI7800_CONDITIONS_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 18070, 2, 9, 1)).setLabel("bTI7800-CONDITIONS-MIB")
bTI7800_CONDITIONS_MIB.setRevisions(('2013-02-19 00:00',))
if mibBuilder.loadTexts: bTI7800_CONDITIONS_MIB.setLastUpdated('201302190000Z')
if mibBuilder.loadTexts: bTI7800_CONDITIONS_MIB.setOrganization('@ORGANIZATION')
class ConfdString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class Severity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("not-alarmed", 4), ("not-reported", 5))

class ConditionCode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135))
    namedValues = NamedValues(("eqptMiss", 1), ("eqptUnkn", 2), ("eqptMism", 3), ("eqptFail", 4), ("eqptDgrd", 5), ("eqptComm", 6), ("upgr", 7), ("lpbk", 8), ("los", 9), ("lof", 10), ("loSync", 11), ("lola", 12), ("lom", 13), ("tim", 14), ("sd", 15), ("bdi", 16), ("pyldMism", 17), ("odtgMism", 18), ("ais-l", 19), ("ms-ais", 20), ("otu-ais", 21), ("odu-ais", 22), ("lck", 23), ("oci", 24), ("highBer", 25), ("lf", 26), ("rf", 27), ("rdi-l", 28), ("ms-rdi", 29), ("oprHighTh", 30), ("oprLowTh", 31), ("optHighTh", 32), ("optLowTh", 33), ("laserTempHighTh", 34), ("laserTempLowTh", 35), ("laserFail", 36), ("cfgUnsupp", 37), ("cfgFail", 38), ("lolightRx", 39), ("lolightTx", 40), ("feim", 41), ("feci", 42), ("contComS", 43), ("contComE", 44), ("loSpecRx", 45), ("tLossRxHt", 46), ("iaocp", 47), ("iaocm", 48), ("iaocb", 49), ("apsd", 50), ("pmi", 51), ("uneqO", 52), ("aisO", 53), ("posRx", 54), ("posTx", 55), ("obros", 56), ("chnDfc", 57), ("replUnitDegrade", 58), ("cnxMea", 59), ("cnxVldTmout", 60), ("posRxHigh", 61), ("posRxLow", 62), ("oprHighFail", 63), ("obrHt", 64), ("apr", 65), ("modTempHighTh", 66), ("modTempLowTh", 67), ("modTempShutdown", 68), ("envTempHighTh", 69), ("envTempLowTh", 70), ("envTempFail", 71), ("envVoltHighTh", 72), ("envVoltLowTh", 73), ("envVoltFail", 74), ("scmNmiDown", 75), ("scmNoNmConn", 76), ("eqptLatchOpen", 77), ("powerAbsent", 78), ("fanSpeedLowTh", 79), ("nonCoLocatedController", 80), ("preFecBerTh", 81), ("firmUpgrdReqd", 82), ("otuBerTh", 83), ("oduBerTh", 84), ("pcsBerTh", 85), ("berTh-s", 86), ("berTh-l", 87), ("rs-berTh", 88), ("ms-berTh", 89), ("oneCableDisconnected", 90), ("envCurrentHighTh", 91), ("envCurrentLowTh", 92), ("prbs", 93), ("forced", 94), ("lockout", 95), ("tLossRxLt", 96), ("omsBdi", 97), ("ochAis", 98), ("ochRdi", 99), ("ochUeq", 100), ("ochOci", 101), ("defRDICCM", 102), ("defMACStatus", 103), ("defRemoteCCM", 104), ("defErrorCCM", 105), ("defXconCCM", 106), ("defBfdDown", 107), ("lf-tx", 108), ("apsData", 109), ("omsAis", 110), ("isisDbOvrld", 111), ("isisXDown", 112), ("isisAdjDown", 113), ("isisAdjRejected", 114), ("rsvpAdjDown", 115), ("diskHighUsage", 116), ("memHighUsage", 117), ("invUnknown", 118), ("airfilterAbsense", 119), ("tx-msais", 120), ("tx-msrdi", 121), ("tx-aisl", 122), ("tx-rdil", 123), ("tx-rf", 124), ("tx-oduAis", 125), ("tx-oduLck", 126), ("tx-oduOci", 127), ("tx-opucsf", 128), ("firmUpgrdInProg", 129), ("firmUpgrdFail", 130), ("partitionFault", 131), ("oom", 132), ("lolck", 133), ("inventoryUnsupp", 134), ("eqptBrownout", 135))

conditionsTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1), )
if mibBuilder.loadTexts: conditionsTable.setStatus('current')
conditionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1), ).setIndexNames((0, "BTI7800-CONDITIONS-MIB", "conditionsEntityName"), (0, "BTI7800-CONDITIONS-MIB", "conditionsCode"))
if mibBuilder.loadTexts: conditionsEntry.setStatus('current')
conditionsEntityName = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 1), String())
if mibBuilder.loadTexts: conditionsEntityName.setStatus('current')
conditionsCode = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 2), ConditionCode())
if mibBuilder.loadTexts: conditionsCode.setStatus('current')
conditionsReportType = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("non-alarmed", 1), ("alarmed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: conditionsReportType.setStatus('current')
conditionsTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: conditionsTimeStamp.setStatus('current')
conditionsSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 5), Severity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: conditionsSeverity.setStatus('current')
conditionsServiceAffecting = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: conditionsServiceAffecting.setStatus('current')
conditionsDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 1, 1, 1, 7), String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: conditionsDescription.setStatus('current')
mibBuilder.exportSymbols("BTI7800-CONDITIONS-MIB", conditionsServiceAffecting=conditionsServiceAffecting, conditionsTable=conditionsTable, conditionsReportType=conditionsReportType, ConfdString=ConfdString, conditionsSeverity=conditionsSeverity, String=String, ConditionCode=ConditionCode, conditionsDescription=conditionsDescription, conditionsCode=conditionsCode, Severity=Severity, conditionsEntityName=conditionsEntityName, PYSNMP_MODULE_ID=bTI7800_CONDITIONS_MIB, conditionsEntry=conditionsEntry, conditionsTimeStamp=conditionsTimeStamp, bTI7800_CONDITIONS_MIB=bTI7800_CONDITIONS_MIB)

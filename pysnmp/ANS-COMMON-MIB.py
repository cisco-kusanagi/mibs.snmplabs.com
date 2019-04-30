#
# PySNMP MIB module ANS-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ANS-COMMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, enterprises, NotificationType, ObjectIdentity, ModuleIdentity, Bits, TimeTicks, Counter64, Gauge32, Counter32, Integer32, MibIdentifier, IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "enterprises", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Bits", "TimeTicks", "Counter64", "Gauge32", "Counter32", "Integer32", "MibIdentifier", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ericsson = MibIdentifier((1, 3, 6, 1, 4, 1, 193))
mlpmp = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 96))
mlpmpR115 = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 96, 115))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 96, 115, 1))
errorMessage = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 2))
class TruthValue(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("true", 1), ("false", 2))

class PhysAddress(OctetString):
    pass

class RowPointer(ObjectIdentifier):
    pass

class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

class DateAndTime(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
errorMessageTable = MibTable((1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 2, 1), )
if mibBuilder.loadTexts: errorMessageTable.setStatus('mandatory')
errorMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 2, 1, 1), ).setIndexNames((0, "ANS-COMMON-MIB", "errorMessageRequestId"))
if mibBuilder.loadTexts: errorMessageEntry.setStatus('mandatory')
errorMessageRequestId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorMessageRequestId.setStatus('mandatory')
errorMessageCode = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorMessageCode.setStatus('mandatory')
mibBuilder.exportSymbols("ANS-COMMON-MIB", errorMessage=errorMessage, errorMessageCode=errorMessageCode, errorMessageTable=errorMessageTable, mlpmp=mlpmp, RowPointer=RowPointer, DateAndTime=DateAndTime, errorMessageRequestId=errorMessageRequestId, RowStatus=RowStatus, ericsson=ericsson, common=common, PhysAddress=PhysAddress, TruthValue=TruthValue, errorMessageEntry=errorMessageEntry, mlpmpR115=mlpmpR115)

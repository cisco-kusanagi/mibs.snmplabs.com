#
# PySNMP MIB module ANS-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ANS-COMMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, IpAddress, Integer32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Counter64, NotificationType, Unsigned32, ObjectIdentity, ModuleIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "IpAddress", "Integer32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Counter64", "NotificationType", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Bits", "Counter32")
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
if mibBuilder.loadTexts: errorMessageTable.setDescription('Table containing additional error information associated with particular SNMP request IDs.')
errorMessageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 2, 1, 1), ).setIndexNames((0, "ANS-COMMON-MIB", "errorMessageRequestId"))
if mibBuilder.loadTexts: errorMessageEntry.setStatus('mandatory')
if mibBuilder.loadTexts: errorMessageEntry.setDescription('Error message associated with a particular request ID.')
errorMessageRequestId = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorMessageRequestId.setStatus('mandatory')
if mibBuilder.loadTexts: errorMessageRequestId.setDescription("The value of the request-id (according to RFC 1157) of the SNMP request response that was received with an error status not equal to 'noError'.")
errorMessageCode = MibTableColumn((1, 3, 6, 1, 4, 1, 193, 96, 115, 1, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: errorMessageCode.setStatus('mandatory')
if mibBuilder.loadTexts: errorMessageCode.setDescription('An error code representing an application specific error message.')
mibBuilder.exportSymbols("ANS-COMMON-MIB", PhysAddress=PhysAddress, ericsson=ericsson, TruthValue=TruthValue, DateAndTime=DateAndTime, errorMessageEntry=errorMessageEntry, errorMessageCode=errorMessageCode, common=common, errorMessageTable=errorMessageTable, errorMessageRequestId=errorMessageRequestId, RowStatus=RowStatus, errorMessage=errorMessage, RowPointer=RowPointer, mlpmp=mlpmp, mlpmpR115=mlpmpR115)

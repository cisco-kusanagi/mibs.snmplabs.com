#
# PySNMP MIB module AIIPVCTABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AIIPVCTABLE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:00:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, TimeTicks, ObjectIdentity, ModuleIdentity, NotificationType, IpAddress, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, iso, MibIdentifier, Counter32, Integer32, Unsigned32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "NotificationType", "IpAddress", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "iso", "MibIdentifier", "Counter32", "Integer32", "Unsigned32", "Counter64")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
class UnsignedShort(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class PositiveInteger(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class IfIndexType(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

aii = MibIdentifier((1, 3, 6, 1, 4, 1, 539))
aiSLC2 = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 16))
aiPVC = ModuleIdentity((1, 3, 6, 1, 4, 1, 539, 16, 1))
if mibBuilder.loadTexts: aiPVC.setLastUpdated('9909141400Z')
if mibBuilder.loadTexts: aiPVC.setOrganization('Applied Innovation Inc.')
class IANAifType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54))
    namedValues = NamedValues(("other", 1), ("regular1822", 2), ("hdh1822", 3), ("ddnX25", 4), ("rfc877x25", 5), ("ethernetCsmacd", 6), ("iso88023Csmacd", 7), ("iso88024TokenBus", 8), ("iso88025TokenRing", 9), ("iso88026Man", 10), ("starLan", 11), ("proteon10Mbit", 12), ("proteon80Mbit", 13), ("hyperchannel", 14), ("fddi", 15), ("lapb", 16), ("sdlc", 17), ("ds1", 18), ("e1", 19), ("basicISDN", 20), ("primaryISDN", 21), ("propPointToPointSerial", 22), ("ppp", 23), ("softwareLoopback", 24), ("eon", 25), ("ethernet3Mbit", 26), ("nsip", 27), ("slip", 28), ("ultra", 29), ("ds3", 30), ("sip", 31), ("frameRelay", 32), ("rs232", 33), ("para", 34), ("arcnet", 35), ("arcnetPlus", 36), ("atm", 37), ("miox25", 38), ("sonet", 39), ("x25ple", 40), ("iso88022llc", 41), ("localTalk", 42), ("smdsDxi", 43), ("frameRelayService", 44), ("v35", 45), ("hssi", 46), ("hippi", 47), ("modem", 48), ("aal5", 49), ("sonetPath", 50), ("sonetVT", 51), ("smdsIcip", 52), ("propVirtual", 53), ("propMultiplexor", 54))

aiPVCTable = MibTable((1, 3, 6, 1, 4, 1, 539, 16, 1, 1), )
if mibBuilder.loadTexts: aiPVCTable.setStatus('current')
aiPVCEntry = MibTableRow((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1), ).setIndexNames((0, "AIIPVCTABLE-MIB", "aiPVCIfType"), (0, "AIIPVCTABLE-MIB", "aiPVCIfIndex"), (0, "AIIPVCTABLE-MIB", "aiPVCCircuit"))
if mibBuilder.loadTexts: aiPVCEntry.setStatus('current')
aiPVCStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 1), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aiPVCStatus.setStatus('current')
aiPVCIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 2), IANAifType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiPVCIfType.setStatus('current')
aiPVCIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 3), IfIndexType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiPVCIfIndex.setStatus('current')
aiPVCCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 4), PositiveInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiPVCCircuit.setStatus('current')
aiPVCCallTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 5), UnsignedShort()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiPVCCallTimer.setStatus('current')
aiPVCInactivityTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 539, 16, 1, 1, 1, 6), UnsignedShort()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aiPVCInactivityTimer.setStatus('current')
aiPVCConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 16, 1, 2))
aiPVCGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 16, 1, 2, 1))
aiPVCCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 539, 16, 1, 2, 2))
aiPVCCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 539, 16, 1, 2, 2, 1)).setObjects(("AIIPVCTABLE-MIB", "aiPVCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aiPVCCompliance = aiPVCCompliance.setStatus('current')
aiPVCGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 539, 16, 1, 2, 1, 1)).setObjects(("AIIPVCTABLE-MIB", "aiPVCStatus"), ("AIIPVCTABLE-MIB", "aiPVCIfIndex"), ("AIIPVCTABLE-MIB", "aiPVCIfType"), ("AIIPVCTABLE-MIB", "aiPVCCircuit"), ("AIIPVCTABLE-MIB", "aiPVCCallTimer"), ("AIIPVCTABLE-MIB", "aiPVCInactivityTimer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aiPVCGroup = aiPVCGroup.setStatus('current')
mibBuilder.exportSymbols("AIIPVCTABLE-MIB", aiPVCEntry=aiPVCEntry, IfIndexType=IfIndexType, aiPVCIfIndex=aiPVCIfIndex, aiPVCGroup=aiPVCGroup, aiPVC=aiPVC, aiPVCStatus=aiPVCStatus, aiPVCGroups=aiPVCGroups, PYSNMP_MODULE_ID=aiPVC, aiPVCConformance=aiPVCConformance, PositiveInteger=PositiveInteger, aiPVCCircuit=aiPVCCircuit, aii=aii, aiSLC2=aiSLC2, UnsignedShort=UnsignedShort, aiPVCCompliances=aiPVCCompliances, aiPVCCallTimer=aiPVCCallTimer, aiPVCCompliance=aiPVCCompliance, aiPVCIfType=aiPVCIfType, aiPVCInactivityTimer=aiPVCInactivityTimer, aiPVCTable=aiPVCTable, IANAifType=IANAifType)

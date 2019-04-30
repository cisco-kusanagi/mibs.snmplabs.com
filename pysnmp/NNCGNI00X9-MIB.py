#
# PySNMP MIB module NNCGNI00X9-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NNCGNI00X9-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:13:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
nncExtSyncDataCct, = mibBuilder.importSymbols("NNCGNI00X1-SMI", "nncExtSyncDataCct")
PositionIndex, = mibBuilder.importSymbols("NNCGNI00X4-MIB", "PositionIndex")
CircuitIndex, PortIndex = mibBuilder.importSymbols("NNCGNI00X7-MIB", "CircuitIndex", "PortIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ObjectIdentity, MibIdentifier, Counter32, IpAddress, ModuleIdentity, Bits, NotificationType, Gauge32, Unsigned32, Integer32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "MibIdentifier", "Counter32", "IpAddress", "ModuleIdentity", "Bits", "NotificationType", "Gauge32", "Unsigned32", "Integer32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class LeadIndex(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("rdl", 1), ("alb", 2), ("rts", 3), ("dtr", 4), ("ri", 5), ("cts", 6), ("dcd", 7), ("dsr", 8))

class LeadAdminState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("forcedOn", 1), ("forcedOff", 2), ("assumedOn", 3), ("assumedOff", 4), ("monitor", 5))

class LeadOperState(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

nncExtSdcTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 14, 1), )
if mibBuilder.loadTexts: nncExtSdcTable.setStatus('mandatory')
nncExtSdcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1), ).setIndexNames((0, "NNCGNI00X9-MIB", "nncExtSdcPosnIdx"), (0, "NNCGNI00X9-MIB", "nncExtSdcPortIdx"), (0, "NNCGNI00X9-MIB", "nncExtSdcCctIdx"))
if mibBuilder.loadTexts: nncExtSdcEntry.setStatus('mandatory')
nncExtSdcPosnIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1, 1), PositionIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSdcPosnIdx.setStatus('mandatory')
nncExtSdcPortIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1, 2), PortIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSdcPortIdx.setStatus('mandatory')
nncExtSdcCctIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1, 3), CircuitIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSdcCctIdx.setStatus('mandatory')
nncExtSdcGender = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dte", 1), ("dce", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtSdcGender.setStatus('mandatory')
nncExtSdcSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2048000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtSdcSpeed.setStatus('mandatory')
nncExtSdcActualSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 14, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2048000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSdcActualSpeed.setStatus('mandatory')
nncExtSdcLeadsTable = MibTable((1, 3, 6, 1, 4, 1, 123, 3, 14, 2), )
if mibBuilder.loadTexts: nncExtSdcLeadsTable.setStatus('mandatory')
nncExtSdcLeadsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 123, 3, 14, 2, 1), ).setIndexNames((0, "NNCGNI00X9-MIB", "nncExtSdcPosnIdx"), (0, "NNCGNI00X9-MIB", "nncExtSdcPortIdx"), (0, "NNCGNI00X9-MIB", "nncExtSdcCctIdx"), (0, "NNCGNI00X9-MIB", "nncExtSdcLeadIdx"))
if mibBuilder.loadTexts: nncExtSdcLeadsEntry.setStatus('mandatory')
nncExtSdcLeadIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 14, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("rdl", 1), ("alb", 2), ("rts", 3), ("dtr", 4), ("ri", 5), ("cts", 6), ("dcd", 7), ("dsr", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSdcLeadIdx.setStatus('mandatory')
nncExtSdcLeadAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 14, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("forcedOn", 1), ("forcedOff", 2), ("assumedOn", 3), ("assumedOff", 4), ("monitor", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nncExtSdcLeadAdminState.setStatus('mandatory')
nncExtSdcLeadOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 14, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSdcLeadOperState.setStatus('mandatory')
nncExtSdcLeadUIName = MibTableColumn((1, 3, 6, 1, 4, 1, 123, 3, 14, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nncExtSdcLeadUIName.setStatus('mandatory')
mibBuilder.exportSymbols("NNCGNI00X9-MIB", nncExtSdcPosnIdx=nncExtSdcPosnIdx, nncExtSdcPortIdx=nncExtSdcPortIdx, nncExtSdcGender=nncExtSdcGender, LeadOperState=LeadOperState, nncExtSdcEntry=nncExtSdcEntry, nncExtSdcLeadIdx=nncExtSdcLeadIdx, nncExtSdcLeadsTable=nncExtSdcLeadsTable, nncExtSdcLeadAdminState=nncExtSdcLeadAdminState, nncExtSdcLeadOperState=nncExtSdcLeadOperState, nncExtSdcLeadsEntry=nncExtSdcLeadsEntry, nncExtSdcSpeed=nncExtSdcSpeed, nncExtSdcTable=nncExtSdcTable, nncExtSdcActualSpeed=nncExtSdcActualSpeed, nncExtSdcCctIdx=nncExtSdcCctIdx, nncExtSdcLeadUIName=nncExtSdcLeadUIName, LeadAdminState=LeadAdminState, LeadIndex=LeadIndex)

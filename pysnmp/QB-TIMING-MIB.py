#
# PySNMP MIB module QB-TIMING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QB-TIMING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:35:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndexOrZero, ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex", "InterfaceIndex")
qbMibs, = mibBuilder.importSymbols("QUANTUMBRIDGE-REG", "qbMibs")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
NotificationType, ObjectIdentity, Integer32, iso, Counter32, Bits, Unsigned32, Counter64, TimeTicks, Gauge32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Integer32", "iso", "Counter32", "Bits", "Unsigned32", "Counter64", "TimeTicks", "Gauge32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, TextualConvention, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue")
qbTimingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4323, 2, 11))
if mibBuilder.loadTexts: qbTimingMIB.setLastUpdated('0101011634Z')
if mibBuilder.loadTexts: qbTimingMIB.setOrganization('Quantum Bridge Inc.')
qbTimingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1))
qbTimingTables = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 11, 2))
qbTimingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 11, 3))
class QbTimingCableLength(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("length0to110ft", 1), ("length110to220ft", 2), ("length220to330ft", 3), ("length330to440ft", 4), ("length440to550ft", 5), ("length550to660ft", 6), ("lengthGreater660ft", 7))

class QbTimingFraming(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("other", 1), ("dsx1ESF", 2), ("dsx1D4", 3), ("dsx1E1", 4), ("dsx1E1CRC", 5), ("dsx1E1MF", 6), ("dsx1E1CRCMF", 7), ("dsx1Unframed", 8), ("dsx1E1Unframed", 9), ("dsx1DS2M12", 10), ("dsx2E2", 11), ("dsx1SF", 12))

class QbTimingPort(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("timing-port1", 1), ("timing-port2", 2))

qbTimingGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1))
qbTimingModeAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 8))).clone(namedValues=NamedValues(("freerun", 1), ("external", 2), ("loop", 3), ("holdover", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbTimingModeAdminStatus.setStatus('current')
qbTimingModeOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("freerun", 1), ("external", 2), ("loop", 3), ("holdoverMntc", 4), ("holdoverAuto", 5), ("notOperational", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qbTimingModeOperStatus.setStatus('current')
qbTimingOutputMode = MibScalar((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disable", 1), ("lock", 2), ("track", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbTimingOutputMode.setStatus('current')
qbTimingHoldoverCtl = MibScalar((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("holdover", 1), ("clearholdover", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbTimingHoldoverCtl.setStatus('current')
qbTimingSourceStatus = MibScalar((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbTimingSourceStatus.setStatus('current')
qbTimingInLineRef = MibScalar((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 6), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbTimingInLineRef.setStatus('current')
qbTimingOutLineRef = MibScalar((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbTimingOutLineRef.setStatus('current')
qbTimingPortTable = MibTable((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8), )
if mibBuilder.loadTexts: qbTimingPortTable.setStatus('current')
qbTimingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1), ).setIndexNames((0, "QB-TIMING-MIB", "qbTimingPort"))
if mibBuilder.loadTexts: qbTimingPortEntry.setStatus('current')
qbTimingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 1), QbTimingPort())
if mibBuilder.loadTexts: qbTimingPort.setStatus('current')
qbTimingPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qbTimingPortName.setStatus('current')
qbTimingPortFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ds1", 1), ("e1", 2), ("noValue", 3))).clone('ds1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbTimingPortFormat.setStatus('current')
qbTimingPortLineCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("dsx1JBZS", 1), ("dsx1B8ZS", 2), ("dsx1HDB3", 3), ("dsx1ZBTSI", 4), ("dsx1AMI", 5), ("other", 6), ("dsx1B6ZS", 7))).clone('dsx1AMI')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbTimingPortLineCoding.setStatus('current')
qbTimingPortFraming = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 5), QbTimingFraming().clone('dsx1SF')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbTimingPortFraming.setStatus('current')
qbTimingPortCableLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 6), QbTimingCableLength().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbTimingPortCableLength.setStatus('current')
qbTimingPortImpedanceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(75, 75), ValueRangeConstraint(120, 120), )).clone(120)).setUnits('in ohms').setMaxAccess("readwrite")
if mibBuilder.loadTexts: qbTimingPortImpedanceMode.setStatus('current')
qbTimingPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("los", 3), ("eqpFailure", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qbTimingPortOperStatus.setStatus('current')
qbTimingPortInOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4323, 2, 11, 1, 1, 8, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("los", 3), ("eqpFailure", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qbTimingPortInOperStatus.setStatus('current')
qbTimingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 11, 3, 1))
qbTimingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 2, 11, 3, 2))
qbTimingCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4323, 2, 11, 3, 1, 1)).setObjects(("QB-TIMING-MIB", "qbTimingAllGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qbTimingCompliance = qbTimingCompliance.setStatus('current')
qbTimingAllGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4323, 2, 11, 3, 2, 1)).setObjects(("QB-TIMING-MIB", "qbTimingModeAdminStatus"), ("QB-TIMING-MIB", "qbTimingModeOperStatus"), ("QB-TIMING-MIB", "qbTimingOutputMode"), ("QB-TIMING-MIB", "qbTimingSourceStatus"), ("QB-TIMING-MIB", "qbTimingHoldoverCtl"), ("QB-TIMING-MIB", "qbTimingSourceStatus"), ("QB-TIMING-MIB", "qbTimingInLineRef"), ("QB-TIMING-MIB", "qbTimingOutLineRef"), ("QB-TIMING-MIB", "qbTimingPortName"), ("QB-TIMING-MIB", "qbTimingPortFormat"), ("QB-TIMING-MIB", "qbTimingPortLineCoding"), ("QB-TIMING-MIB", "qbTimingPortFraming"), ("QB-TIMING-MIB", "qbTimingPortCableLength"), ("QB-TIMING-MIB", "qbTimingPortImpedanceMode"), ("QB-TIMING-MIB", "qbTimingPortOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qbTimingAllGroup = qbTimingAllGroup.setStatus('current')
mibBuilder.exportSymbols("QB-TIMING-MIB", QbTimingCableLength=QbTimingCableLength, qbTimingPortFormat=qbTimingPortFormat, qbTimingModeAdminStatus=qbTimingModeAdminStatus, qbTimingPortEntry=qbTimingPortEntry, qbTimingModeOperStatus=qbTimingModeOperStatus, qbTimingHoldoverCtl=qbTimingHoldoverCtl, qbTimingMIB=qbTimingMIB, qbTimingGroup=qbTimingGroup, qbTimingCompliance=qbTimingCompliance, qbTimingObjects=qbTimingObjects, qbTimingPort=qbTimingPort, QbTimingPort=QbTimingPort, qbTimingAllGroup=qbTimingAllGroup, qbTimingSourceStatus=qbTimingSourceStatus, qbTimingTables=qbTimingTables, qbTimingPortImpedanceMode=qbTimingPortImpedanceMode, qbTimingPortLineCoding=qbTimingPortLineCoding, qbTimingPortTable=qbTimingPortTable, qbTimingPortName=qbTimingPortName, qbTimingOutputMode=qbTimingOutputMode, qbTimingPortFraming=qbTimingPortFraming, qbTimingPortInOperStatus=qbTimingPortInOperStatus, qbTimingPortOperStatus=qbTimingPortOperStatus, qbTimingCompliances=qbTimingCompliances, qbTimingConformance=qbTimingConformance, QbTimingFraming=QbTimingFraming, qbTimingInLineRef=qbTimingInLineRef, qbTimingPortCableLength=qbTimingPortCableLength, PYSNMP_MODULE_ID=qbTimingMIB, qbTimingGroups=qbTimingGroups, qbTimingOutLineRef=qbTimingOutLineRef)

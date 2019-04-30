#
# PySNMP MIB module PDN-IFDEV-IWF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-IFDEV-IWF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:30:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_interfaces, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-interfaces")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, IpAddress, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, Integer32, iso, NotificationType, ModuleIdentity, Gauge32, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "Integer32", "iso", "NotificationType", "ModuleIdentity", "Gauge32", "Counter32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pdnIfDevIwfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27))
pdnIfDevIwfMIB.setRevisions(('2004-09-10 00:00',))
if mibBuilder.loadTexts: pdnIfDevIwfMIB.setLastUpdated('200409100000Z')
if mibBuilder.loadTexts: pdnIfDevIwfMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
pdnIfDevIwfNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 0))
pdnIfDevIwfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1))
pdnIfDevIwfAFNs = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 2))
pdnIfDevIwfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3))
class TxRxUnit(TextualConvention, Integer32):
    reference = "RFC 1662, Section 1.2, `Terminology'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("bits", 2), ("octets", 3), ("frames", 4), ("packets", 5), ("datagrams", 6))

pdnIfDevIwfStatsTotalTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1), )
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalTable.setStatus('current')
pdnIfDevIwfStatsTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalEntry.setStatus('current')
pdnIfDevIwfStatsTotalBufferUnderruns = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalBufferUnderruns.setStatus('current')
pdnIfDevIwfStatsTotalMRUErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalMRUErrors.setStatus('current')
pdnIfDevIwfStatsTotalRxUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 3), TxRxUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalRxUnit.setStatus('current')
pdnIfDevIwfStatsTotalRx = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pdnIfDevIwfStatsTotalRx.setStatus('current')
pdnIfDevIwfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 1))
pdnIfDevIwfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2))
pdnIfDevIwfCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 1, 1)).setObjects(("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalBufferUnderrunsGroup"), ("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalMRUErrorsGroup"), ("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalRxGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfDevIwfCompliance = pdnIfDevIwfCompliance.setStatus('current')
pdnIfDevIwfObjGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1))
pdnIfDevIwfAfnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 2))
pdnIfDevIwfNtfyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 3))
pdnIfDevIwfStatsTotalBufferUnderrunsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1, 1)).setObjects(("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalBufferUnderruns"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfDevIwfStatsTotalBufferUnderrunsGroup = pdnIfDevIwfStatsTotalBufferUnderrunsGroup.setStatus('current')
pdnIfDevIwfStatsTotalMRUErrorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1, 2)).setObjects(("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalMRUErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfDevIwfStatsTotalMRUErrorsGroup = pdnIfDevIwfStatsTotalMRUErrorsGroup.setStatus('current')
pdnIfDevIwfStatsTotalRxGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 27, 3, 2, 1, 3)).setObjects(("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalRxUnit"), ("PDN-IFDEV-IWF-MIB", "pdnIfDevIwfStatsTotalRx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnIfDevIwfStatsTotalRxGroup = pdnIfDevIwfStatsTotalRxGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-IFDEV-IWF-MIB", PYSNMP_MODULE_ID=pdnIfDevIwfMIB, pdnIfDevIwfStatsTotalRxUnit=pdnIfDevIwfStatsTotalRxUnit, pdnIfDevIwfObjects=pdnIfDevIwfObjects, pdnIfDevIwfStatsTotalTable=pdnIfDevIwfStatsTotalTable, pdnIfDevIwfStatsTotalMRUErrorsGroup=pdnIfDevIwfStatsTotalMRUErrorsGroup, TxRxUnit=TxRxUnit, pdnIfDevIwfCompliance=pdnIfDevIwfCompliance, pdnIfDevIwfStatsTotalMRUErrors=pdnIfDevIwfStatsTotalMRUErrors, pdnIfDevIwfStatsTotalRx=pdnIfDevIwfStatsTotalRx, pdnIfDevIwfMIB=pdnIfDevIwfMIB, pdnIfDevIwfAFNs=pdnIfDevIwfAFNs, pdnIfDevIwfAfnGroups=pdnIfDevIwfAfnGroups, pdnIfDevIwfStatsTotalBufferUnderrunsGroup=pdnIfDevIwfStatsTotalBufferUnderrunsGroup, pdnIfDevIwfStatsTotalEntry=pdnIfDevIwfStatsTotalEntry, pdnIfDevIwfObjGroups=pdnIfDevIwfObjGroups, pdnIfDevIwfGroups=pdnIfDevIwfGroups, pdnIfDevIwfNtfyGroups=pdnIfDevIwfNtfyGroups, pdnIfDevIwfNotifications=pdnIfDevIwfNotifications, pdnIfDevIwfStatsTotalRxGroup=pdnIfDevIwfStatsTotalRxGroup, pdnIfDevIwfStatsTotalBufferUnderruns=pdnIfDevIwfStatsTotalBufferUnderruns, pdnIfDevIwfConformance=pdnIfDevIwfConformance, pdnIfDevIwfCompliances=pdnIfDevIwfCompliances)

#
# PySNMP MIB module RBN-ATM-CELL-PW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBN-ATM-CELL-PW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:52:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
RbnCircuitHandle, = mibBuilder.importSymbols("RBN-TC", "RbnCircuitHandle")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Counter32, MibIdentifier, TimeTicks, Gauge32, ModuleIdentity, Unsigned32, iso, IpAddress, Bits, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Counter32", "MibIdentifier", "TimeTicks", "Gauge32", "ModuleIdentity", "Unsigned32", "iso", "IpAddress", "Bits", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbnAtmCellPWMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 41))
rbnAtmCellPWMIB.setRevisions(('2007-05-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnAtmCellPWMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: rbnAtmCellPWMIB.setLastUpdated('200705300000Z')
if mibBuilder.loadTexts: rbnAtmCellPWMIB.setOrganization('Redback Networks, Inc.')
if mibBuilder.loadTexts: rbnAtmCellPWMIB.setContactInfo(' Redback Networks, Inc. Postal: 300 Holger Way San Jose, CA 95134 USA Phone: +1 408 750 5000 Fax: +1 408 750 5599 E-mail: mib-info@redback.com ')
if mibBuilder.loadTexts: rbnAtmCellPWMIB.setDescription('The MIB for managing the ATM Cell Pseudo Wire circuits that are used to carry ATM traffic. ')
rbnAtmCellPWObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 41, 1))
rbnAtmCellPWStatTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1), )
if mibBuilder.loadTexts: rbnAtmCellPWStatTable.setStatus('current')
if mibBuilder.loadTexts: rbnAtmCellPWStatTable.setDescription('This table provides a collection of objects providing statistics of a ATM Cell Pseudo wire circuit that is used to carry ATM traffic.')
rbnAtmCellPWStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1, 1), ).setIndexNames((0, "RBN-ATM-CELL-PW-MIB", "rbnAtmCellPWCircuitHandle"))
if mibBuilder.loadTexts: rbnAtmCellPWStatEntry.setStatus('current')
if mibBuilder.loadTexts: rbnAtmCellPWStatEntry.setDescription('Each entry in this table represents a statistics per ATM Cell Pseudo Wire circuit. This table is indexed by Pseudo Wire circuit handle. ')
rbnAtmCellPWCircuitHandle = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1, 1, 1), RbnCircuitHandle())
if mibBuilder.loadTexts: rbnAtmCellPWCircuitHandle.setStatus('current')
if mibBuilder.loadTexts: rbnAtmCellPWCircuitHandle.setDescription('A key for identifing the PW circuit. See the definition of the RbnCircuitHandle TEXTUAL-CONVENTION for the definition of this circuit handle.')
rbnAtmCellPWOutOfSeqDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAtmCellPWOutOfSeqDrops.setStatus('current')
if mibBuilder.loadTexts: rbnAtmCellPWOutOfSeqDrops.setDescription('The total number of cells that dropped because of out-of-sequence PDUs received on the PW circuit.')
rbnAtmCellPWCellConcatDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 41, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnAtmCellPWCellConcatDrops.setStatus('current')
if mibBuilder.loadTexts: rbnAtmCellPWCellConcatDrops.setDescription('The total number of cells that dropped because of cell-concatenated PDUs received on the PW circuit.')
rbnAtmCellPWMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 41, 2))
rbnAtmCellPWMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 41, 2, 1))
rbnAtmCellPWMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 41, 2, 2))
rbnAtmCellPWMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 41, 2, 2, 1)).setObjects(("RBN-ATM-CELL-PW-MIB", "rbnAtmCellPWStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmCellPWMIBCompliance = rbnAtmCellPWMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: rbnAtmCellPWMIBCompliance.setDescription('The compliance statement for RedBack Networks SNMP entities which represent ATM Cell PW circuit.')
rbnAtmCellPWStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 41, 2, 1, 1)).setObjects(("RBN-ATM-CELL-PW-MIB", "rbnAtmCellPWOutOfSeqDrops"), ("RBN-ATM-CELL-PW-MIB", "rbnAtmCellPWCellConcatDrops"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnAtmCellPWStatGroup = rbnAtmCellPWStatGroup.setStatus('current')
if mibBuilder.loadTexts: rbnAtmCellPWStatGroup.setDescription('The collection of objects which represent PW circuit statistics.')
mibBuilder.exportSymbols("RBN-ATM-CELL-PW-MIB", rbnAtmCellPWCellConcatDrops=rbnAtmCellPWCellConcatDrops, rbnAtmCellPWMIBCompliance=rbnAtmCellPWMIBCompliance, rbnAtmCellPWOutOfSeqDrops=rbnAtmCellPWOutOfSeqDrops, PYSNMP_MODULE_ID=rbnAtmCellPWMIB, rbnAtmCellPWMIBConformance=rbnAtmCellPWMIBConformance, rbnAtmCellPWStatEntry=rbnAtmCellPWStatEntry, rbnAtmCellPWMIB=rbnAtmCellPWMIB, rbnAtmCellPWStatGroup=rbnAtmCellPWStatGroup, rbnAtmCellPWMIBCompliances=rbnAtmCellPWMIBCompliances, rbnAtmCellPWMIBGroups=rbnAtmCellPWMIBGroups, rbnAtmCellPWObjects=rbnAtmCellPWObjects, rbnAtmCellPWCircuitHandle=rbnAtmCellPWCircuitHandle, rbnAtmCellPWStatTable=rbnAtmCellPWStatTable)

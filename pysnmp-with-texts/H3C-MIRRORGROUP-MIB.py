#
# PySNMP MIB module H3C-MIRRORGROUP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-MIRRORGROUP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:23:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, TimeTicks, ModuleIdentity, Unsigned32, MibIdentifier, iso, Counter64, Bits, Counter32, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "TimeTicks", "ModuleIdentity", "Unsigned32", "MibIdentifier", "iso", "Counter64", "Bits", "Counter32", "Gauge32", "ObjectIdentity")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
h3cMirrGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68))
h3cMirrGroup.setRevisions(('2006-01-10 19:03',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cMirrGroup.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: h3cMirrGroup.setLastUpdated('200601131403Z')
if mibBuilder.loadTexts: h3cMirrGroup.setOrganization('Huawei 3Com Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cMirrGroup.setContactInfo('Platform Team Huawei 3Com Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085 ')
if mibBuilder.loadTexts: h3cMirrGroup.setDescription('This MIB defines objects for managing mirror group.')
h3cMGInfoObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1))
h3cMGObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1))
h3cMGTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1, 1), )
if mibBuilder.loadTexts: h3cMGTable.setStatus('current')
if mibBuilder.loadTexts: h3cMGTable.setDescription('A list of mirror group entries.')
h3cMGEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1, 1, 1), ).setIndexNames((0, "H3C-MIRRORGROUP-MIB", "h3cMGID"))
if mibBuilder.loadTexts: h3cMGEntry.setStatus('current')
if mibBuilder.loadTexts: h3cMGEntry.setDescription('A list of parameters that describe a mirror group to be created.')
h3cMGID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cMGID.setStatus('current')
if mibBuilder.loadTexts: h3cMGID.setDescription('An index that uniquely identifies an entry in the mirror group table.')
h3cMGType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("local", 1), ("remoteSource", 2), ("remoteDestination", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMGType.setStatus('current')
if mibBuilder.loadTexts: h3cMGType.setDescription('GroupType.')
h3cMGStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cMGStatus.setStatus('current')
if mibBuilder.loadTexts: h3cMGStatus.setDescription('The status of a mirror group. A mirror group will be inactive when it was created. The status of a mirror group can be changed automatically from inactive to active when appropriate conditions were met, also, it can be changed automatically from active to inactive when these conditions disappeared. Followings are conditions for a mirror group to become active: group type conditions ============================================================================ local mirroring-port, monitor-port remoteSource mirroring-port, remote-probe vlan, reflector-port(may not be supported by some products) remoteDestination monitor-port, remote-probe vlan ')
h3cMGRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMGRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cMGRowStatus.setDescription('RowStatus')
h3cMGMirrorIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 2))
h3cMGMirrorIfTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 2, 1), )
if mibBuilder.loadTexts: h3cMGMirrorIfTable.setStatus('current')
if mibBuilder.loadTexts: h3cMGMirrorIfTable.setDescription('A list of mirror group mirroring-port entries.')
h3cMGMirrorIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 2, 1, 1), ).setIndexNames((0, "H3C-MIRRORGROUP-MIB", "h3cMGID"), (0, "H3C-MIRRORGROUP-MIB", "h3cMGMirrorIfIndex"), (0, "H3C-MIRRORGROUP-MIB", "h3cMGMirrorDirection"))
if mibBuilder.loadTexts: h3cMGMirrorIfEntry.setStatus('current')
if mibBuilder.loadTexts: h3cMGMirrorIfEntry.setDescription('A list of parameters that describe a mirroring-port to be added to a mirror group.')
h3cMGMirrorIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cMGMirrorIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cMGMirrorIfIndex.setDescription('IfIndex of mirror group mirroring-port.')
h3cMGMirrorDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inbound", 1), ("outbound", 2), ("both", 3))))
if mibBuilder.loadTexts: h3cMGMirrorDirection.setStatus('current')
if mibBuilder.loadTexts: h3cMGMirrorDirection.setDescription("Mirror direction of mirroring-port. Once mirror direction was configured for a mirroring-port, it can not be changed unless the mirroring-port was removed from mirror group. If a mirror port is configured with two mirror directions 'outbound' and 'inbound', though it is functionally equal to 'both', it will be handled as two table items. If a mirror port is configured with mirror direction 'outbound' or 'inbound', or both of them, it will not be allowed to configure 'both', more details please refer to mirror group manual.")
h3cMGMirrorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 2, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMGMirrorRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cMGMirrorRowStatus.setDescription('RowStatus')
h3cMGMonitorIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 3))
h3cMGMonitorIfTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 3, 1), )
if mibBuilder.loadTexts: h3cMGMonitorIfTable.setStatus('current')
if mibBuilder.loadTexts: h3cMGMonitorIfTable.setDescription('A list of mirror group monitor-port entries.')
h3cMGMonitorIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 3, 1, 1), ).setIndexNames((0, "H3C-MIRRORGROUP-MIB", "h3cMGID"), (0, "H3C-MIRRORGROUP-MIB", "h3cMGMonitorIfIndex"))
if mibBuilder.loadTexts: h3cMGMonitorIfEntry.setStatus('current')
if mibBuilder.loadTexts: h3cMGMonitorIfEntry.setDescription('A list of parameters that describe a monitor-port to be added to a mirror group.')
h3cMGMonitorIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cMGMonitorIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cMGMonitorIfIndex.setDescription('IfIndex of mirror group monitor-port.')
h3cMGMonitorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 3, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMGMonitorRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cMGMonitorRowStatus.setDescription('RowStatus')
h3cMGReflectorIfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 4))
h3cMGReflectorIfTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 4, 1), )
if mibBuilder.loadTexts: h3cMGReflectorIfTable.setStatus('current')
if mibBuilder.loadTexts: h3cMGReflectorIfTable.setDescription('A list of mirror group reflector-port entries.')
h3cMGReflectorIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 4, 1, 1), ).setIndexNames((0, "H3C-MIRRORGROUP-MIB", "h3cMGID"), (0, "H3C-MIRRORGROUP-MIB", "h3cMGReflectorIfIndex"))
if mibBuilder.loadTexts: h3cMGReflectorIfEntry.setStatus('current')
if mibBuilder.loadTexts: h3cMGReflectorIfEntry.setDescription('A list of parameters that describe a reflector-port to be added to a mirror group.')
h3cMGReflectorIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 4, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cMGReflectorIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cMGReflectorIfIndex.setDescription('IfIndex of mirror group reflector-port.')
h3cMGReflectorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 4, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMGReflectorRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cMGReflectorRowStatus.setDescription('RowStatus')
h3cMGRprobeVlanObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 5))
h3cMGRprobeVlanTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 5, 1), )
if mibBuilder.loadTexts: h3cMGRprobeVlanTable.setStatus('current')
if mibBuilder.loadTexts: h3cMGRprobeVlanTable.setDescription('A list of mirror group remote-probe vlan entries.')
h3cMGRprobeVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 5, 1, 1), ).setIndexNames((0, "H3C-MIRRORGROUP-MIB", "h3cMGID"), (0, "H3C-MIRRORGROUP-MIB", "h3cMGRprobeVlanID"))
if mibBuilder.loadTexts: h3cMGRprobeVlanEntry.setStatus('current')
if mibBuilder.loadTexts: h3cMGRprobeVlanEntry.setDescription('A list of parameters that describe a remote-probe vlan to be added to a mirror group. Details about remote-probe vlan please refer to mirror group manual.')
h3cMGRprobeVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: h3cMGRprobeVlanID.setStatus('current')
if mibBuilder.loadTexts: h3cMGRprobeVlanID.setDescription('An index that uniquely identifies an entry in the remote-probe vlan table.')
h3cMGRprobeVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 68, 1, 5, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cMGRprobeVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cMGRprobeVlanRowStatus.setDescription('RowStatus')
mibBuilder.exportSymbols("H3C-MIRRORGROUP-MIB", h3cMGRprobeVlanObjects=h3cMGRprobeVlanObjects, h3cMGStatus=h3cMGStatus, h3cMGMirrorDirection=h3cMGMirrorDirection, h3cMGInfoObjects=h3cMGInfoObjects, h3cMGMirrorIfEntry=h3cMGMirrorIfEntry, h3cMGMonitorIfEntry=h3cMGMonitorIfEntry, h3cMGMonitorIfIndex=h3cMGMonitorIfIndex, h3cMGReflectorIfIndex=h3cMGReflectorIfIndex, h3cMGType=h3cMGType, h3cMGReflectorIfEntry=h3cMGReflectorIfEntry, h3cMGMonitorIfObjects=h3cMGMonitorIfObjects, h3cMGRowStatus=h3cMGRowStatus, h3cMGReflectorRowStatus=h3cMGReflectorRowStatus, h3cMirrGroup=h3cMirrGroup, h3cMGMirrorIfIndex=h3cMGMirrorIfIndex, h3cMGTable=h3cMGTable, h3cMGMirrorRowStatus=h3cMGMirrorRowStatus, h3cMGEntry=h3cMGEntry, h3cMGMirrorIfObjects=h3cMGMirrorIfObjects, h3cMGMonitorIfTable=h3cMGMonitorIfTable, h3cMGMirrorIfTable=h3cMGMirrorIfTable, h3cMGID=h3cMGID, h3cMGReflectorIfObjects=h3cMGReflectorIfObjects, PYSNMP_MODULE_ID=h3cMirrGroup, h3cMGObjects=h3cMGObjects, h3cMGRprobeVlanRowStatus=h3cMGRprobeVlanRowStatus, h3cMGRprobeVlanEntry=h3cMGRprobeVlanEntry, h3cMGReflectorIfTable=h3cMGReflectorIfTable, h3cMGRprobeVlanID=h3cMGRprobeVlanID, h3cMGMonitorRowStatus=h3cMGMonitorRowStatus, h3cMGRprobeVlanTable=h3cMGRprobeVlanTable)

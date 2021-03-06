#
# PySNMP MIB module HPN-ICF-PEX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-PEX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:28:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
entPhysicalIndex, entPhysicalDescr = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "entPhysicalDescr")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, MibIdentifier, Counter64, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, IpAddress, NotificationType, Bits, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "MibIdentifier", "Counter64", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "IpAddress", "NotificationType", "Bits", "Counter32", "ModuleIdentity")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hpnicfPex = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129))
hpnicfPex.setRevisions(('2012-11-12 11:29',))
if mibBuilder.loadTexts: hpnicfPex.setLastUpdated('201211121129Z')
if mibBuilder.loadTexts: hpnicfPex.setOrganization('')
hpnicfPexSpecInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 1))
hpnicfPexPortMinId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPexPortMinId.setStatus('current')
hpnicfPexPortMaxId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPexPortMaxId.setStatus('current')
hpnicfPexMinAssociateId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPexMinAssociateId.setStatus('current')
hpnicfPexMaxAssociateId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPexMaxAssociateId.setStatus('current')
hpnicfPexMaxPortPerPexPort = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPexMaxPortPerPexPort.setStatus('current')
hpnicfPexTable = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2))
hpnicfPexPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1), )
if mibBuilder.loadTexts: hpnicfPexPortTable.setStatus('current')
hpnicfPexPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1), ).setIndexNames((0, "HPN-ICF-PEX-MIB", "hpnicfPexPortId"))
if mibBuilder.loadTexts: hpnicfPexPortEntry.setStatus('current')
hpnicfPexPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfPexPortId.setStatus('current')
hpnicfPexPortAssociateId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1, 2), Integer32().clone(65535)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfPexPortAssociateId.setStatus('current')
hpnicfPexPortEntPhysicalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPexPortEntPhysicalIndex.setStatus('current')
hpnicfPexPortDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 79))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfPexPortDescr.setStatus('current')
hpnicfPexPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("offline", 1), ("loading", 2), ("online", 3))).clone('offline')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPexPortStatus.setStatus('current')
hpnicfPexPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfPexPortRowStatus.setStatus('current')
hpnicfPexPhyPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 2), )
if mibBuilder.loadTexts: hpnicfPexPhyPortTable.setStatus('current')
hpnicfPexPhyPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpnicfPexPhyPortEntry.setStatus('current')
hpnicfPexPhyPortStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("down", 2), ("blocked", 3), ("forwarding", 4))).clone('unknown')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPexPhyPortStatus.setStatus('current')
hpnicfPexPhyPortBelongToPexPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfPexPhyPortBelongToPexPort.setStatus('current')
hpnicfPexPhyPortNeighborEntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfPexPhyPortNeighborEntIndex.setStatus('current')
hpnicfPexTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 3))
hpnicfPexTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 3, 0))
hpnicfPexPortOnline = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 3, 0, 1)).setObjects(("HPN-ICF-PEX-MIB", "hpnicfPexPortId"), ("HPN-ICF-PEX-MIB", "hpnicfPexPortDescr"))
if mibBuilder.loadTexts: hpnicfPexPortOnline.setStatus('current')
hpnicfPexPortOffline = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 3, 0, 2)).setObjects(("HPN-ICF-PEX-MIB", "hpnicfPexPortId"), ("HPN-ICF-PEX-MIB", "hpnicfPexPortDescr"))
if mibBuilder.loadTexts: hpnicfPexPortOffline.setStatus('current')
hpnicfPexPhyPortForwarding = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 3, 0, 3)).setObjects(("HPN-ICF-PEX-MIB", "hpnicfPexEntPhysicalIndexBind"), ("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: hpnicfPexPhyPortForwarding.setStatus('current')
hpnicfPexPhyPortBlocked = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 3, 0, 4)).setObjects(("HPN-ICF-PEX-MIB", "hpnicfPexEntPhysicalIndexBind"), ("ENTITY-MIB", "entPhysicalDescr"))
if mibBuilder.loadTexts: hpnicfPexPhyPortBlocked.setStatus('current')
hpnicfPexTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 4))
hpnicfPexEntPhysicalIndexBind = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 129, 4, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpnicfPexEntPhysicalIndexBind.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-PEX-MIB", hpnicfPexPortDescr=hpnicfPexPortDescr, hpnicfPexMaxPortPerPexPort=hpnicfPexMaxPortPerPexPort, hpnicfPexTraps=hpnicfPexTraps, hpnicfPexMaxAssociateId=hpnicfPexMaxAssociateId, hpnicfPexPhyPortForwarding=hpnicfPexPhyPortForwarding, hpnicfPexPortOnline=hpnicfPexPortOnline, hpnicfPex=hpnicfPex, hpnicfPexPortOffline=hpnicfPexPortOffline, hpnicfPexPortAssociateId=hpnicfPexPortAssociateId, hpnicfPexPortId=hpnicfPexPortId, hpnicfPexPortEntry=hpnicfPexPortEntry, hpnicfPexTrapObjects=hpnicfPexTrapObjects, hpnicfPexPortRowStatus=hpnicfPexPortRowStatus, hpnicfPexPhyPortBlocked=hpnicfPexPhyPortBlocked, hpnicfPexTable=hpnicfPexTable, hpnicfPexTrapPrefix=hpnicfPexTrapPrefix, PYSNMP_MODULE_ID=hpnicfPex, hpnicfPexPortEntPhysicalIndex=hpnicfPexPortEntPhysicalIndex, hpnicfPexPortMinId=hpnicfPexPortMinId, hpnicfPexPortStatus=hpnicfPexPortStatus, hpnicfPexPhyPortStatus=hpnicfPexPhyPortStatus, hpnicfPexSpecInfo=hpnicfPexSpecInfo, hpnicfPexPhyPortNeighborEntIndex=hpnicfPexPhyPortNeighborEntIndex, hpnicfPexPhyPortBelongToPexPort=hpnicfPexPhyPortBelongToPexPort, hpnicfPexEntPhysicalIndexBind=hpnicfPexEntPhysicalIndexBind, hpnicfPexPhyPortEntry=hpnicfPexPhyPortEntry, hpnicfPexPortTable=hpnicfPexPortTable, hpnicfPexPortMaxId=hpnicfPexPortMaxId, hpnicfPexPhyPortTable=hpnicfPexPhyPortTable, hpnicfPexMinAssociateId=hpnicfPexMinAssociateId)

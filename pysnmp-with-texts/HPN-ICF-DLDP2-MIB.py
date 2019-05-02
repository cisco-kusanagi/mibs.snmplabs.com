#
# PySNMP MIB module HPN-ICF-DLDP2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-DLDP2-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:37:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifDescr, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifDescr", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Integer32, TimeTicks, MibIdentifier, Bits, Counter32, ModuleIdentity, Counter64, Unsigned32, ObjectIdentity, iso, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "TimeTicks", "MibIdentifier", "Bits", "Counter32", "ModuleIdentity", "Counter64", "Unsigned32", "ObjectIdentity", "iso", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
MacAddress, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TruthValue", "TextualConvention")
hpnicfDldp2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117))
hpnicfDldp2.setRevisions(('2011-12-26 15:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfDldp2.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: hpnicfDldp2.setLastUpdated('201112261530Z')
if mibBuilder.loadTexts: hpnicfDldp2.setOrganization('')
if mibBuilder.loadTexts: hpnicfDldp2.setContactInfo('')
if mibBuilder.loadTexts: hpnicfDldp2.setDescription('Device Link Detection Protocol (DLDP) MIB. Device Link Detection Protocol is a private Layer 2 protocol, which can be used to detect and shut down unidirectional links (fiber or copper links) to avoid network problems.')
hpnicfDldp2ScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 1))
hpnicfDldp2GlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDldp2GlobalEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2GlobalEnable.setDescription('Enable(true) or disable(false) DLDP on the device.')
hpnicfDldp2Interval = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(5)).setUnits('second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDldp2Interval.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2Interval.setDescription('Indicates the advertisement packet sending interval.')
hpnicfDldp2AuthMode = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("none", 2), ("simple", 3), ("md5", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDldp2AuthMode.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2AuthMode.setDescription('Indicates the authentication mode. unknown: cannot be determined for some reason. none: not authenticated. simple: authenticated by a clear text password. md5: authenticated by MD5 digest.')
hpnicfDldp2AuthPassword = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDldp2AuthPassword.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2AuthPassword.setDescription('Indicates the authentication password. Setting the password to a zero-length octet string means deleting the password. When read, it always returns a zero-length octet string.')
hpnicfDldp2UniShutdown = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("auto", 2), ("manual", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDldp2UniShutdown.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2UniShutdown.setDescription('Indicates the shutdown mode when a unidirectional link has been detected. unknown: cannot be determined for some reason. auto: the port will be shutdown automatically. manual: the port must be shut down manually.')
hpnicfDldp2TableGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2))
hpnicfDldp2PortConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 1), )
if mibBuilder.loadTexts: hpnicfDldp2PortConfigTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2PortConfigTable.setDescription('This table contains all ports that support DLDP.')
hpnicfDldp2PortConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfDldp2PortConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2PortConfigEntry.setDescription('This entry describes a port that supports DLDP.')
hpnicfDldp2PortEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDldp2PortEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2PortEnable.setDescription('Enable(true) or disable(false) DLDP on a port.')
hpnicfDldp2PortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 2), )
if mibBuilder.loadTexts: hpnicfDldp2PortStatusTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2PortStatusTable.setDescription('This table contains all ports enabled with DLDP.')
hpnicfDldp2PortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfDldp2PortStatusEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2PortStatusEntry.setDescription('This entry describes a port enabled with DLDP.')
hpnicfDldp2PortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("initial", 2), ("inactive", 3), ("unidirectional", 4), ("bidirectional", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDldp2PortOperStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2PortOperStatus.setDescription("Indicates the DLDP operating status on the port. unknown: cannot be determined for some reason. initial: DLDP is not globally enabled. inactive: physical status of the port is down. unidirectional: all neighbors of the port are in 'unconfirmed' status. bidirectional: more than one neighbor of the port is in 'confirmed' status.")
hpnicfDldp2PortLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("down", 2), ("up", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDldp2PortLinkStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2PortLinkStatus.setDescription("Indicates the DLDP link status of the port. unknown: cannot be determined for some reason. down: the DLDP link status of the port is down. up: the DLDP link status of the port is up. If the port operating status is not 'inactive', 'unidirectional', or 'bidirectional', it always returns 'unknown'.")
hpnicfDldp2NeighborTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 3), )
if mibBuilder.loadTexts: hpnicfDldp2NeighborTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2NeighborTable.setDescription("This table contains all port's neighbors.")
hpnicfDldp2NeighborEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HPN-ICF-DLDP2-MIB", "hpnicfDldp2NeighborBridgeMac"), (0, "HPN-ICF-DLDP2-MIB", "hpnicfDldp2NeighborPortIndex"))
if mibBuilder.loadTexts: hpnicfDldp2NeighborEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2NeighborEntry.setDescription("This entry describes a port's neighbors.")
hpnicfDldp2NeighborBridgeMac = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 3, 1, 1), MacAddress())
if mibBuilder.loadTexts: hpnicfDldp2NeighborBridgeMac.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2NeighborBridgeMac.setDescription('Indicates the bridge MAC address of a neighbor.')
hpnicfDldp2NeighborPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: hpnicfDldp2NeighborPortIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2NeighborPortIndex.setDescription('Indicates the port index of a neighbor.')
hpnicfDldp2NeighborStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("unconfirmed", 2), ("confirmed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDldp2NeighborStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2NeighborStatus.setDescription('Indicates the status of a neighbor. unknown: cannot be determined for some reason. unconfirmed: unidirectional communication between the port and its neighbor. confirmed: bidirectional communication between the port and its neighbor.')
hpnicfDldp2NeighborAgingTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 3, 1, 4), Integer32()).setUnits('second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDldp2NeighborAgingTime.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2NeighborAgingTime.setDescription("Indicates the aging time of a neighbor. If the neighbor status is not 'confirmed', it always returns 0.")
hpnicfDldp2TrapBindObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 3))
hpnicfDldp2Trap = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 4))
hpnicfDldp2TrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 4, 0))
hpnicfDldp2TrapUniLink = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 4, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hpnicfDldp2TrapUniLink.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2TrapUniLink.setDescription('This trap is generated when DLDP detects a unidirectional link, ifIndex and ifDescr identify the port.')
hpnicfDldp2TrapBidLink = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 4, 0, 2)).setObjects(("IF-MIB", "ifIndex"), ("IF-MIB", "ifDescr"))
if mibBuilder.loadTexts: hpnicfDldp2TrapBidLink.setStatus('current')
if mibBuilder.loadTexts: hpnicfDldp2TrapBidLink.setDescription('This trap is generated when DLDP detects a bidirectional link, ifIndex and ifDescr identify the port.')
mibBuilder.exportSymbols("HPN-ICF-DLDP2-MIB", hpnicfDldp2PortConfigTable=hpnicfDldp2PortConfigTable, hpnicfDldp2NeighborStatus=hpnicfDldp2NeighborStatus, hpnicfDldp2AuthMode=hpnicfDldp2AuthMode, hpnicfDldp2NeighborEntry=hpnicfDldp2NeighborEntry, hpnicfDldp2PortConfigEntry=hpnicfDldp2PortConfigEntry, hpnicfDldp2PortOperStatus=hpnicfDldp2PortOperStatus, hpnicfDldp2TrapBindObjects=hpnicfDldp2TrapBindObjects, hpnicfDldp2PortStatusEntry=hpnicfDldp2PortStatusEntry, hpnicfDldp2NeighborAgingTime=hpnicfDldp2NeighborAgingTime, hpnicfDldp2UniShutdown=hpnicfDldp2UniShutdown, hpnicfDldp2NeighborTable=hpnicfDldp2NeighborTable, hpnicfDldp2Trap=hpnicfDldp2Trap, hpnicfDldp2NeighborPortIndex=hpnicfDldp2NeighborPortIndex, hpnicfDldp2Interval=hpnicfDldp2Interval, hpnicfDldp2TrapBidLink=hpnicfDldp2TrapBidLink, hpnicfDldp2PortLinkStatus=hpnicfDldp2PortLinkStatus, hpnicfDldp2AuthPassword=hpnicfDldp2AuthPassword, hpnicfDldp2ScalarGroup=hpnicfDldp2ScalarGroup, hpnicfDldp2TableGroup=hpnicfDldp2TableGroup, hpnicfDldp2PortEnable=hpnicfDldp2PortEnable, PYSNMP_MODULE_ID=hpnicfDldp2, hpnicfDldp2TrapPrefix=hpnicfDldp2TrapPrefix, hpnicfDldp2PortStatusTable=hpnicfDldp2PortStatusTable, hpnicfDldp2GlobalEnable=hpnicfDldp2GlobalEnable, hpnicfDldp2=hpnicfDldp2, hpnicfDldp2NeighborBridgeMac=hpnicfDldp2NeighborBridgeMac, hpnicfDldp2TrapUniLink=hpnicfDldp2TrapUniLink)

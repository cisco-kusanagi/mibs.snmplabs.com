#
# PySNMP MIB module Dell-Private-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-Private-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:56:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
ipAddrEntry, = mibBuilder.importSymbols("IP-MIB", "ipAddrEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibIdentifier, IpAddress, ModuleIdentity, Counter32, Counter64, ObjectIdentity, Unsigned32, Integer32, TimeTicks, Bits, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "IpAddress", "ModuleIdentity", "Counter32", "Counter64", "ObjectIdentity", "Unsigned32", "Integer32", "TimeTicks", "Bits", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlOperationalMode = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 121))
rlOperationalMode.setRevisions(('2006-11-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlOperationalMode.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlOperationalMode.setLastUpdated('200611010000Z')
if mibBuilder.loadTexts: rlOperationalMode.setOrganization('Dell')
if mibBuilder.loadTexts: rlOperationalMode.setContactInfo('www.dell.com')
if mibBuilder.loadTexts: rlOperationalMode.setDescription('The private MIB module definition for operational mode.')
rlOperationalModeState = MibScalar((1, 3, 6, 1, 4, 1, 89, 121, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("managed", 0), ("unmanaged", 1), ("secure", 2))).clone('managed')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlOperationalModeState.setStatus('current')
if mibBuilder.loadTexts: rlOperationalModeState.setDescription('Show/Set the current Operational Mode state')
rlGlobalIpAddrTable = MibTable((1, 3, 6, 1, 4, 1, 89, 121, 2), )
if mibBuilder.loadTexts: rlGlobalIpAddrTable.setStatus('current')
if mibBuilder.loadTexts: rlGlobalIpAddrTable.setDescription('This table is parralel to MIB II IpAddrTable, and is used to add/delete entries to/from that table.')
rlGlobalIpAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 121, 2, 1), ).setIndexNames((0, "Dell-Private-MIB", "rlGlobalIpAdIndex"))
if mibBuilder.loadTexts: rlGlobalIpAddrEntry.setStatus('current')
if mibBuilder.loadTexts: rlGlobalIpAddrEntry.setDescription('The system global IP address information.')
rlGlobalIpAdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlGlobalIpAdIndex.setStatus('current')
if mibBuilder.loadTexts: rlGlobalIpAdIndex.setDescription('The system global IP address index.')
rlGlobalIpAdEntAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGlobalIpAdEntAddr.setStatus('current')
if mibBuilder.loadTexts: rlGlobalIpAdEntAddr.setDescription("The IP address to which this entry's addressing information pertains.")
rlGlobalIpAdEntNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGlobalIpAdEntNetMask.setStatus('current')
if mibBuilder.loadTexts: rlGlobalIpAdEntNetMask.setDescription('The subnet mask associated with the system global IP address. The value of the mask is an IP address with all the network bits set to 1 and all the hosts bits set to 0.')
rlGlobalIpAdDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGlobalIpAdDefaultGateway.setStatus('current')
if mibBuilder.loadTexts: rlGlobalIpAdDefaultGateway.setDescription(' The default gateway of the system global IP address ')
rlGlobalIpAdOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 121, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("dhcp", 2), ("default", 3))).clone('static')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlGlobalIpAdOwner.setStatus('current')
if mibBuilder.loadTexts: rlGlobalIpAdOwner.setDescription('The IP Interface owner. Static if interface defined by user, dhcp if received by boot protocol like DHCP.')
rlDeleteUsersAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 89, 121, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("false", 0), ("true", 1))).clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDeleteUsersAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlDeleteUsersAfterReset.setDescription('Remove all entries from the rlAAALocalUserTable after reset')
mibBuilder.exportSymbols("Dell-Private-MIB", rlGlobalIpAdEntAddr=rlGlobalIpAdEntAddr, PYSNMP_MODULE_ID=rlOperationalMode, rlGlobalIpAdEntNetMask=rlGlobalIpAdEntNetMask, rlDeleteUsersAfterReset=rlDeleteUsersAfterReset, rlGlobalIpAdOwner=rlGlobalIpAdOwner, rlGlobalIpAdDefaultGateway=rlGlobalIpAdDefaultGateway, rlGlobalIpAddrTable=rlGlobalIpAddrTable, rlGlobalIpAdIndex=rlGlobalIpAdIndex, rlOperationalMode=rlOperationalMode, rlGlobalIpAddrEntry=rlGlobalIpAddrEntry, rlOperationalModeState=rlOperationalModeState)

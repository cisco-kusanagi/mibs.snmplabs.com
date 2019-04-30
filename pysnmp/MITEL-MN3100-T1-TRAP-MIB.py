#
# PySNMP MIB module MITEL-MN3100-T1-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MITEL-MN3100-T1-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:03:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
dsx1LineStatus, = mibBuilder.importSymbols("RFC1406-MIB", "dsx1LineStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Gauge32, Counter32, NotificationType, Bits, IpAddress, iso, ModuleIdentity, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, enterprises, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Gauge32", "Counter32", "NotificationType", "Bits", "IpAddress", "iso", "ModuleIdentity", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "enterprises", "ObjectIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mitelDS1Extension = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 12))
mitelDS1Extension.setRevisions(('2003-03-24 01:41', '2002-04-02 00:00',))
if mibBuilder.loadTexts: mitelDS1Extension.setLastUpdated('200204020000Z')
if mibBuilder.loadTexts: mitelDS1Extension.setOrganization('MITEL Networks Corporation')
mitel = MibIdentifier((1, 3, 6, 1, 4, 1, 1027))
mitelProprietary = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 4))
mitelIdentification = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1))
mitelIdCallServers = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2))
mitelIdCsIpera1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4))
mitelIpera1000Notifications = NotificationGroup((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0)).setObjects(("MITEL-MN3100-T1-TRAP-MIB", "mitelMn3100dsx1LineSatusChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mitelIpera1000Notifications = mitelIpera1000Notifications.setStatus('current')
mitelMn3100dsx1LineSatusChangeNotif = NotificationType((1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 410)).setObjects(("RFC1406-MIB", "dsx1LineStatus"))
if mibBuilder.loadTexts: mitelMn3100dsx1LineSatusChangeNotif.setStatus('current')
mibBuilder.exportSymbols("MITEL-MN3100-T1-TRAP-MIB", mitelIdentification=mitelIdentification, mitelProprietary=mitelProprietary, mitelMn3100dsx1LineSatusChangeNotif=mitelMn3100dsx1LineSatusChangeNotif, PYSNMP_MODULE_ID=mitelDS1Extension, mitelDS1Extension=mitelDS1Extension, mitelIdCsIpera1000=mitelIdCsIpera1000, mitelIdCallServers=mitelIdCallServers, mitel=mitel, mitelIpera1000Notifications=mitelIpera1000Notifications)

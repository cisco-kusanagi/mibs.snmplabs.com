#
# PySNMP MIB module TPLINK-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-LLDP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, Gauge32, IpAddress, Unsigned32, NotificationType, Counter64, iso, ObjectIdentity, TimeTicks, Bits, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "Gauge32", "IpAddress", "Unsigned32", "NotificationType", "Counter64", "iso", "ObjectIdentity", "TimeTicks", "Bits", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkLldpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 35))
tplinkLldpMIB.setRevisions(('2012-12-13 17:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkLldpMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkLldpMIB.setLastUpdated('201212131730Z')
if mibBuilder.loadTexts: tplinkLldpMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkLldpMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkLldpMIB.setDescription('LLDP Private MIB.')
tplinkLldpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 35, 1))
tplinkLldpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 35, 2))
mibBuilder.exportSymbols("TPLINK-LLDP-MIB", tplinkLldpMIB=tplinkLldpMIB, PYSNMP_MODULE_ID=tplinkLldpMIB, tplinkLldpMIBNotifications=tplinkLldpMIBNotifications, tplinkLldpMIBObjects=tplinkLldpMIBObjects)

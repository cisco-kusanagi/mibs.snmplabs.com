#
# PySNMP MIB module TPLINK-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-SNMP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:25:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, TimeTicks, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Integer32, Bits, ModuleIdentity, Unsigned32, iso, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Integer32", "Bits", "ModuleIdentity", "Unsigned32", "iso", "NotificationType", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkSnmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 32))
tplinkSnmpMIB.setRevisions(('2009-08-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkSnmpMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkSnmpMIB.setLastUpdated('201212140000Z')
if mibBuilder.loadTexts: tplinkSnmpMIB.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkSnmpMIB.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkSnmpMIB.setDescription('Private MIB for snmp config.')
tplinkSnmpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1))
tplinkSnmpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 32, 2))
mibBuilder.exportSymbols("TPLINK-SNMP-MIB", tplinkSnmpMIB=tplinkSnmpMIB, tplinkSnmpMIBNotifications=tplinkSnmpMIBNotifications, PYSNMP_MODULE_ID=tplinkSnmpMIB, tplinkSnmpMIBObjects=tplinkSnmpMIBObjects)

#
# PySNMP MIB module TPLINK-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-SNMP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, iso, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Gauge32, ModuleIdentity, NotificationType, ObjectIdentity, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "iso", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Gauge32", "ModuleIdentity", "NotificationType", "ObjectIdentity", "TimeTicks", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkSnmpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 32))
tplinkSnmpMIB.setRevisions(('2009-08-19 00:00',))
if mibBuilder.loadTexts: tplinkSnmpMIB.setLastUpdated('201212140000Z')
if mibBuilder.loadTexts: tplinkSnmpMIB.setOrganization('TPLINK')
tplinkSnmpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 32, 1))
tplinkSnmpMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 32, 2))
mibBuilder.exportSymbols("TPLINK-SNMP-MIB", tplinkSnmpMIBObjects=tplinkSnmpMIBObjects, PYSNMP_MODULE_ID=tplinkSnmpMIB, tplinkSnmpMIB=tplinkSnmpMIB, tplinkSnmpMIBNotifications=tplinkSnmpMIBNotifications)

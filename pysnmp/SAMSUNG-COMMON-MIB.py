#
# PySNMP MIB module SAMSUNG-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SAMSUNG-COMMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:52:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, enterprises, Integer32, NotificationType, TimeTicks, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Bits, Unsigned32, Counter64, MibIdentifier, Gauge32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "Integer32", "NotificationType", "TimeTicks", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Bits", "Unsigned32", "Counter64", "MibIdentifier", "Gauge32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
samsung = ModuleIdentity((1, 3, 6, 1, 4, 1, 236))
if mibBuilder.loadTexts: samsung.setLastUpdated('0209170000Z')
if mibBuilder.loadTexts: samsung.setOrganization('Samsung Corporation - Samsung DPD Solution SW Team')
division = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11))
if mibBuilder.loadTexts: division.setStatus('current')
oadivision = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5))
if mibBuilder.loadTexts: oadivision.setStatus('current')
samsungCommonMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 236, 11, 5, 11))
if mibBuilder.loadTexts: samsungCommonMIB.setStatus('current')
mibBuilder.exportSymbols("SAMSUNG-COMMON-MIB", samsungCommonMIB=samsungCommonMIB, division=division, oadivision=oadivision, PYSNMP_MODULE_ID=samsung, samsung=samsung)

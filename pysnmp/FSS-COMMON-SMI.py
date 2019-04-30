#
# PySNMP MIB module FSS-COMMON-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FSS-COMMON-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 19:02:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, IpAddress, TimeTicks, Counter64, Bits, Integer32, ObjectIdentity, iso, Counter32, Unsigned32, NotificationType, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "IpAddress", "TimeTicks", "Counter64", "Bits", "Integer32", "ObjectIdentity", "iso", "Counter32", "Unsigned32", "NotificationType", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fujitsu = ModuleIdentity((1, 3, 6, 1, 4, 1, 211))
if mibBuilder.loadTexts: fujitsu.setLastUpdated('201605131500Z')
if mibBuilder.loadTexts: fujitsu.setOrganization('Fujitsu Network Communications, Inc.')
product = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1))
transport = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24))
fssCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 211, 1, 24, 12))
mibBuilder.exportSymbols("FSS-COMMON-SMI", transport=transport, product=product, fssCommon=fssCommon, PYSNMP_MODULE_ID=fujitsu, fujitsu=fujitsu)

#
# PySNMP MIB module HUAWEI-WLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-WLAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:38:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
huaweiUtility, = mibBuilder.importSymbols("HUAWEI-MIB", "huaweiUtility")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, IpAddress, Counter64, Counter32, Integer32, Bits, MibIdentifier, NotificationType, ObjectIdentity, Unsigned32, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "IpAddress", "Counter64", "Counter32", "Integer32", "Bits", "MibIdentifier", "NotificationType", "ObjectIdentity", "Unsigned32", "Gauge32", "ModuleIdentity")
RowStatus, DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "DateAndTime", "TextualConvention")
hwWlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 6, 139))
hwWlan.setRevisions(('2010-06-08 00:00',))
if mibBuilder.loadTexts: hwWlan.setLastUpdated('201006080000Z')
if mibBuilder.loadTexts: hwWlan.setOrganization('Huawei Technologies Co.,Ltd.')
mibBuilder.exportSymbols("HUAWEI-WLAN-MIB", hwWlan=hwWlan, PYSNMP_MODULE_ID=hwWlan)

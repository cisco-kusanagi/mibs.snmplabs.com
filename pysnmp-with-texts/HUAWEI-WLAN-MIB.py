#
# PySNMP MIB module HUAWEI-WLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-WLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
huaweiUtility, = mibBuilder.importSymbols("HUAWEI-MIB", "huaweiUtility")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, Gauge32, ObjectIdentity, Unsigned32, Bits, IpAddress, NotificationType, iso, MibIdentifier, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "Bits", "IpAddress", "NotificationType", "iso", "MibIdentifier", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, RowStatus, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "DateAndTime", "TextualConvention")
hwWlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 6, 139))
hwWlan.setRevisions(('2010-06-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwWlan.setRevisionsDescriptions((' V1.00, Inital version. ',))
if mibBuilder.loadTexts: hwWlan.setLastUpdated('201006080000Z')
if mibBuilder.loadTexts: hwWlan.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwWlan.setContactInfo("Huawei Industrial Base Bantian, Longgang Shenzhen 518129 People's Republic of China Website: http://www.huawei.com Email: support@huawei.com ")
if mibBuilder.loadTexts: hwWlan.setDescription('This mib defines the root node of the wlan mib')
mibBuilder.exportSymbols("HUAWEI-WLAN-MIB", PYSNMP_MODULE_ID=hwWlan, hwWlan=hwWlan)

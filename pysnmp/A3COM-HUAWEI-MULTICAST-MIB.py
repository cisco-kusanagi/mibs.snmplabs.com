#
# PySNMP MIB module A3COM-HUAWEI-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:51:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, NotificationType, Gauge32, ObjectIdentity, Unsigned32, IpAddress, Counter32, MibIdentifier, iso, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "NotificationType", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter32", "MibIdentifier", "iso", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cMulticast = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 50))
h3cMulticast.setRevisions(('2005-04-29 00:00',))
if mibBuilder.loadTexts: h3cMulticast.setLastUpdated('200504290000Z')
if mibBuilder.loadTexts: h3cMulticast.setOrganization('Huawei 3Com Technologies Co., Ltd.')
class EnabledStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

h3cMulticastObject = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 50, 1))
h3cMulticastEnable = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 50, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cMulticastEnable.setStatus('current')
mibBuilder.exportSymbols("A3COM-HUAWEI-MULTICAST-MIB", h3cMulticastEnable=h3cMulticastEnable, EnabledStatus=EnabledStatus, PYSNMP_MODULE_ID=h3cMulticast, h3cMulticast=h3cMulticast, h3cMulticastObject=h3cMulticastObject)

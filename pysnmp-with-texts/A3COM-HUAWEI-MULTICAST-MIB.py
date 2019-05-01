#
# PySNMP MIB module A3COM-HUAWEI-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:06:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
h3cCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "h3cCommon")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, IpAddress, iso, Bits, Gauge32, Integer32, MibIdentifier, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "IpAddress", "iso", "Bits", "Gauge32", "Integer32", "MibIdentifier", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cMulticast = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 50))
h3cMulticast.setRevisions(('2005-04-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cMulticast.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: h3cMulticast.setLastUpdated('200504290000Z')
if mibBuilder.loadTexts: h3cMulticast.setOrganization('Huawei 3Com Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cMulticast.setContactInfo('Platform Team Huawei 3Com Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.huawei-3com.com Zip:100085')
if mibBuilder.loadTexts: h3cMulticast.setDescription('The multicast global configuration MIB')
class EnabledStatus(TextualConvention, Integer32):
    description = 'A simple status value for the object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

h3cMulticastObject = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 50, 1))
h3cMulticastEnable = MibScalar((1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 50, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cMulticastEnable.setStatus('current')
if mibBuilder.loadTexts: h3cMulticastEnable.setDescription('To enable or disable global multicast.')
mibBuilder.exportSymbols("A3COM-HUAWEI-MULTICAST-MIB", h3cMulticast=h3cMulticast, h3cMulticastObject=h3cMulticastObject, h3cMulticastEnable=h3cMulticastEnable, PYSNMP_MODULE_ID=h3cMulticast, EnabledStatus=EnabledStatus)

#
# PySNMP MIB module H3C-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:23:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Counter32, Gauge32, Counter64, ObjectIdentity, IpAddress, MibIdentifier, NotificationType, Bits, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Counter32", "Gauge32", "Counter64", "ObjectIdentity", "IpAddress", "MibIdentifier", "NotificationType", "Bits", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cMulticast = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 50))
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

h3cMulticastObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 50, 1))
h3cMulticastEnable = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 50, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cMulticastEnable.setStatus('current')
if mibBuilder.loadTexts: h3cMulticastEnable.setDescription('To enable or disable global multicast.')
mibBuilder.exportSymbols("H3C-MULTICAST-MIB", h3cMulticastObject=h3cMulticastObject, h3cMulticast=h3cMulticast, PYSNMP_MODULE_ID=h3cMulticast, EnabledStatus=EnabledStatus, h3cMulticastEnable=h3cMulticastEnable)

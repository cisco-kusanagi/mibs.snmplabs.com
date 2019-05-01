#
# PySNMP MIB module HPN-ICF-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:40:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, IpAddress, Integer32, iso, Counter64, NotificationType, Unsigned32, Gauge32, MibIdentifier, TimeTicks, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "IpAddress", "Integer32", "iso", "Counter64", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier", "TimeTicks", "Bits", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfMulticast = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 50))
hpnicfMulticast.setRevisions(('2005-04-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfMulticast.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: hpnicfMulticast.setLastUpdated('200504290000Z')
if mibBuilder.loadTexts: hpnicfMulticast.setOrganization('')
if mibBuilder.loadTexts: hpnicfMulticast.setContactInfo('')
if mibBuilder.loadTexts: hpnicfMulticast.setDescription('The multicast global configuration MIB')
class EnabledStatus(TextualConvention, Integer32):
    description = 'A simple status value for the object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hpnicfMulticastObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 50, 1))
hpnicfMulticastEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 50, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfMulticastEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfMulticastEnable.setDescription('To enable or disable global multicast.')
mibBuilder.exportSymbols("HPN-ICF-MULTICAST-MIB", PYSNMP_MODULE_ID=hpnicfMulticast, EnabledStatus=EnabledStatus, hpnicfMulticast=hpnicfMulticast, hpnicfMulticastObject=hpnicfMulticastObject, hpnicfMulticastEnable=hpnicfMulticastEnable)

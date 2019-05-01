#
# PySNMP MIB module HH3C-MULTICAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-MULTICAST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:28:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, NotificationType, Unsigned32, iso, Counter64, TimeTicks, Integer32, ObjectIdentity, ModuleIdentity, MibIdentifier, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "NotificationType", "Unsigned32", "iso", "Counter64", "TimeTicks", "Integer32", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "IpAddress", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cMulticast = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 50))
hh3cMulticast.setRevisions(('2005-04-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cMulticast.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: hh3cMulticast.setLastUpdated('200504290000Z')
if mibBuilder.loadTexts: hh3cMulticast.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cMulticast.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cMulticast.setDescription('The multicast global configuration MIB')
class EnabledStatus(TextualConvention, Integer32):
    description = 'A simple status value for the object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hh3cMulticastObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 50, 1))
hh3cMulticastEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 50, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cMulticastEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cMulticastEnable.setDescription('To enable or disable global multicast.')
mibBuilder.exportSymbols("HH3C-MULTICAST-MIB", hh3cMulticastObject=hh3cMulticastObject, EnabledStatus=EnabledStatus, PYSNMP_MODULE_ID=hh3cMulticast, hh3cMulticast=hh3cMulticast, hh3cMulticastEnable=hh3cMulticastEnable)

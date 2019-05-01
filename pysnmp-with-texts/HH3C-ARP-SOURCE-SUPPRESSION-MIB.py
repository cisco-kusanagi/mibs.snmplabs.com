#
# PySNMP MIB module HH3C-ARP-SOURCE-SUPPRESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-ARP-SOURCE-SUPPRESSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:25:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Counter64, Unsigned32, iso, ObjectIdentity, Bits, IpAddress, Counter32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Counter64", "Unsigned32", "iso", "ObjectIdentity", "Bits", "IpAddress", "Counter32", "ModuleIdentity", "NotificationType")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
hh3cARPSourceSuppression = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 146))
hh3cARPSourceSuppression.setRevisions(('2013-10-14 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cARPSourceSuppression.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: hh3cARPSourceSuppression.setLastUpdated('201310141800Z')
if mibBuilder.loadTexts: hh3cARPSourceSuppression.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: hh3cARPSourceSuppression.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip: 100085')
if mibBuilder.loadTexts: hh3cARPSourceSuppression.setDescription('This MIB file is to provide the definition of the ARP source suppression. ')
hh3cARPSourceSuppressionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 146, 1))
hh3cARPSourceSuppressionGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 146, 1, 1))
hh3cARPSourceSuppressionEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 146, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cARPSourceSuppressionEnable.setStatus('current')
if mibBuilder.loadTexts: hh3cARPSourceSuppressionEnable.setDescription('Enable or disable ARP source suppression function.')
hh3cARPSourceSuppressionLimit = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 146, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 1024)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cARPSourceSuppressionLimit.setStatus('current')
if mibBuilder.loadTexts: hh3cARPSourceSuppressionLimit.setDescription('Set the maximum number of unresolvable packets that the device can receive from a device in five seconds.')
mibBuilder.exportSymbols("HH3C-ARP-SOURCE-SUPPRESSION-MIB", hh3cARPSourceSuppressionGlobal=hh3cARPSourceSuppressionGlobal, hh3cARPSourceSuppression=hh3cARPSourceSuppression, hh3cARPSourceSuppressionEnable=hh3cARPSourceSuppressionEnable, hh3cARPSourceSuppressionLimit=hh3cARPSourceSuppressionLimit, hh3cARPSourceSuppressionObjects=hh3cARPSourceSuppressionObjects, PYSNMP_MODULE_ID=hh3cARPSourceSuppression)

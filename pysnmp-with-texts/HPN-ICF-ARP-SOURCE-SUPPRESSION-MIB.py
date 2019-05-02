#
# PySNMP MIB module HPN-ICF-ARP-SOURCE-SUPPRESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-ARP-SOURCE-SUPPRESSION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:37:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Counter32, MibIdentifier, ObjectIdentity, ModuleIdentity, iso, NotificationType, Integer32, Counter64, Bits, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Counter32", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "NotificationType", "Integer32", "Counter64", "Bits", "TimeTicks", "Gauge32")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
hpnicfARPSourceSuppression = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146))
hpnicfARPSourceSuppression.setRevisions(('2013-10-14 18:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfARPSourceSuppression.setRevisionsDescriptions(('The initial version of this MIB file.',))
if mibBuilder.loadTexts: hpnicfARPSourceSuppression.setLastUpdated('201310141800Z')
if mibBuilder.loadTexts: hpnicfARPSourceSuppression.setOrganization('')
if mibBuilder.loadTexts: hpnicfARPSourceSuppression.setContactInfo('')
if mibBuilder.loadTexts: hpnicfARPSourceSuppression.setDescription('This MIB file is to provide the definition of the ARP source suppression. ')
hpnicfARPSourceSuppressionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1))
hpnicfARPSourceSuppressionGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1, 1))
hpnicfARPSourceSuppressionEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfARPSourceSuppressionEnable.setStatus('current')
if mibBuilder.loadTexts: hpnicfARPSourceSuppressionEnable.setDescription('Enable or disable ARP source suppression function.')
hpnicfARPSourceSuppressionLimit = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 1024)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfARPSourceSuppressionLimit.setStatus('current')
if mibBuilder.loadTexts: hpnicfARPSourceSuppressionLimit.setDescription('Set the maximum number of unresolvable packets that the device can receive from a device in five seconds.')
mibBuilder.exportSymbols("HPN-ICF-ARP-SOURCE-SUPPRESSION-MIB", PYSNMP_MODULE_ID=hpnicfARPSourceSuppression, hpnicfARPSourceSuppressionObjects=hpnicfARPSourceSuppressionObjects, hpnicfARPSourceSuppressionEnable=hpnicfARPSourceSuppressionEnable, hpnicfARPSourceSuppression=hpnicfARPSourceSuppression, hpnicfARPSourceSuppressionGlobal=hpnicfARPSourceSuppressionGlobal, hpnicfARPSourceSuppressionLimit=hpnicfARPSourceSuppressionLimit)

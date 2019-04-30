#
# PySNMP MIB module HPN-ICF-ARP-SOURCE-SUPPRESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-ARP-SOURCE-SUPPRESSION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:25:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, Gauge32, Unsigned32, ModuleIdentity, Counter32, iso, TimeTicks, Integer32, NotificationType, IpAddress, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Gauge32", "Unsigned32", "ModuleIdentity", "Counter32", "iso", "TimeTicks", "Integer32", "NotificationType", "IpAddress", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
hpnicfARPSourceSuppression = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146))
hpnicfARPSourceSuppression.setRevisions(('2013-10-14 18:00',))
if mibBuilder.loadTexts: hpnicfARPSourceSuppression.setLastUpdated('201310141800Z')
if mibBuilder.loadTexts: hpnicfARPSourceSuppression.setOrganization('')
hpnicfARPSourceSuppressionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1))
hpnicfARPSourceSuppressionGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1, 1))
hpnicfARPSourceSuppressionEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfARPSourceSuppressionEnable.setStatus('current')
hpnicfARPSourceSuppressionLimit = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 1024)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfARPSourceSuppressionLimit.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-ARP-SOURCE-SUPPRESSION-MIB", hpnicfARPSourceSuppressionLimit=hpnicfARPSourceSuppressionLimit, hpnicfARPSourceSuppression=hpnicfARPSourceSuppression, hpnicfARPSourceSuppressionGlobal=hpnicfARPSourceSuppressionGlobal, PYSNMP_MODULE_ID=hpnicfARPSourceSuppression, hpnicfARPSourceSuppressionEnable=hpnicfARPSourceSuppressionEnable, hpnicfARPSourceSuppressionObjects=hpnicfARPSourceSuppressionObjects)

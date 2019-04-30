#
# PySNMP MIB module HH3C-ARP-SOURCE-SUPPRESSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-ARP-SOURCE-SUPPRESSION-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:12:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Bits, NotificationType, TimeTicks, Counter64, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, MibIdentifier, iso, ModuleIdentity, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "NotificationType", "TimeTicks", "Counter64", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "MibIdentifier", "iso", "ModuleIdentity", "Gauge32", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
hh3cARPSourceSuppression = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 146))
hh3cARPSourceSuppression.setRevisions(('2013-10-14 18:00',))
if mibBuilder.loadTexts: hh3cARPSourceSuppression.setLastUpdated('201310141800Z')
if mibBuilder.loadTexts: hh3cARPSourceSuppression.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
hh3cARPSourceSuppressionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 146, 1))
hh3cARPSourceSuppressionGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 146, 1, 1))
hh3cARPSourceSuppressionEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 146, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cARPSourceSuppressionEnable.setStatus('current')
hh3cARPSourceSuppressionLimit = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 146, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 1024)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cARPSourceSuppressionLimit.setStatus('current')
mibBuilder.exportSymbols("HH3C-ARP-SOURCE-SUPPRESSION-MIB", hh3cARPSourceSuppressionGlobal=hh3cARPSourceSuppressionGlobal, hh3cARPSourceSuppressionObjects=hh3cARPSourceSuppressionObjects, PYSNMP_MODULE_ID=hh3cARPSourceSuppression, hh3cARPSourceSuppressionEnable=hh3cARPSourceSuppressionEnable, hh3cARPSourceSuppression=hh3cARPSourceSuppression, hh3cARPSourceSuppressionLimit=hh3cARPSourceSuppressionLimit)

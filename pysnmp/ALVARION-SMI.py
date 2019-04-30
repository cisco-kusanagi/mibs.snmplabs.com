#
# PySNMP MIB module ALVARION-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ALVARION-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 17:06:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Unsigned32, ObjectIdentity, TimeTicks, MibIdentifier, Integer32, ModuleIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Gauge32, NotificationType, Counter32, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Integer32", "ModuleIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Gauge32", "NotificationType", "Counter32", "Counter64", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
alvarionWireless = ModuleIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10))
if mibBuilder.loadTexts: alvarionWireless.setLastUpdated('200710310000Z')
if mibBuilder.loadTexts: alvarionWireless.setOrganization('Alvarion Ltd.')
alvarionProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 1))
if mibBuilder.loadTexts: alvarionProducts.setStatus('current')
alvarionExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 3))
if mibBuilder.loadTexts: alvarionExperiment.setStatus('current')
alvarionModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 4))
if mibBuilder.loadTexts: alvarionModules.setStatus('current')
alvarionMgmtV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 5))
if mibBuilder.loadTexts: alvarionMgmtV2.setStatus('current')
variation = ObjectIdentity((1, 3, 6, 1, 4, 1, 12394, 1, 10, 7))
if mibBuilder.loadTexts: variation.setStatus('current')
mibBuilder.exportSymbols("ALVARION-SMI", variation=variation, PYSNMP_MODULE_ID=alvarionWireless, alvarionProducts=alvarionProducts, alvarionWireless=alvarionWireless, alvarionModules=alvarionModules, alvarionMgmtV2=alvarionMgmtV2, alvarionExperiment=alvarionExperiment)

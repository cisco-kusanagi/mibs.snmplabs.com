#
# PySNMP MIB module HPN-ICF-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-FIREWALL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:26:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, MibIdentifier, Counter64, iso, TimeTicks, Integer32, Unsigned32, NotificationType, IpAddress, ModuleIdentity, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "MibIdentifier", "Counter64", "iso", "TimeTicks", "Integer32", "Unsigned32", "NotificationType", "IpAddress", "ModuleIdentity", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfFireWall = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88))
if mibBuilder.loadTexts: hpnicfFireWall.setLastUpdated('200801171450Z')
if mibBuilder.loadTexts: hpnicfFireWall.setOrganization('')
hpnicfFirewallobject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1))
hpnicfFirewallSpecs = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 1))
hpnicfFWMaxConnNum = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFWMaxConnNum.setStatus('current')
hpnicfFirewallGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 2))
hpnicfFWConnNumCurr = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFWConnNumCurr.setStatus('current')
hpnicfFWConnRate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfFWConnRate.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-FIREWALL-MIB", hpnicfFirewallGlobalStats=hpnicfFirewallGlobalStats, hpnicfFWMaxConnNum=hpnicfFWMaxConnNum, hpnicfFirewallobject=hpnicfFirewallobject, hpnicfFireWall=hpnicfFireWall, hpnicfFWConnRate=hpnicfFWConnRate, hpnicfFWConnNumCurr=hpnicfFWConnNumCurr, hpnicfFirewallSpecs=hpnicfFirewallSpecs, PYSNMP_MODULE_ID=hpnicfFireWall)

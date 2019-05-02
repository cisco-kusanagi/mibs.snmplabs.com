#
# PySNMP MIB module HH3C-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-FIREWALL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:27:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, TimeTicks, Counter64, Counter32, iso, IpAddress, Gauge32, Unsigned32, MibIdentifier, ObjectIdentity, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "TimeTicks", "Counter64", "Counter32", "iso", "IpAddress", "Gauge32", "Unsigned32", "MibIdentifier", "ObjectIdentity", "NotificationType", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hh3cFireWall = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 88))
if mibBuilder.loadTexts: hh3cFireWall.setLastUpdated('200801171450Z')
if mibBuilder.loadTexts: hh3cFireWall.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cFireWall.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: hh3cFireWall.setDescription('The MIB is designed to manage H3C Firewall products.')
hh3cFirewallobject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 88, 1))
hh3cFirewallSpecs = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 1))
hh3cFWMaxConnNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFWMaxConnNum.setStatus('current')
if mibBuilder.loadTexts: hh3cFWMaxConnNum.setDescription('Max connection number of system.')
hh3cFirewallGlobalStats = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 2))
hh3cFWConnNumCurr = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 88, 1, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cFWConnNumCurr.setStatus('current')
if mibBuilder.loadTexts: hh3cFWConnNumCurr.setDescription('The number of connections that currently exist.')
mibBuilder.exportSymbols("HH3C-FIREWALL-MIB", hh3cFirewallobject=hh3cFirewallobject, hh3cFirewallGlobalStats=hh3cFirewallGlobalStats, hh3cFWMaxConnNum=hh3cFWMaxConnNum, hh3cFireWall=hh3cFireWall, PYSNMP_MODULE_ID=hh3cFireWall, hh3cFWConnNumCurr=hh3cFWConnNumCurr, hh3cFirewallSpecs=hh3cFirewallSpecs)

#
# PySNMP MIB module NOVELSAT-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NOVELSAT-ROOT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:14:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, ModuleIdentity, IpAddress, Gauge32, enterprises, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, Counter32, Counter64, ObjectIdentity, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "IpAddress", "Gauge32", "enterprises", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "Counter32", "Counter64", "ObjectIdentity", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nsRoot = ModuleIdentity((1, 3, 6, 1, 4, 1, 37576))
nsRoot.setRevisions(('2010-09-12 15:00',))
if mibBuilder.loadTexts: nsRoot.setLastUpdated('201009121500Z')
if mibBuilder.loadTexts: nsRoot.setOrganization('Novelsat')
nsMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 37576, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsMibVersion.setStatus('current')
mibBuilder.exportSymbols("NOVELSAT-ROOT-MIB", PYSNMP_MODULE_ID=nsRoot, nsMibVersion=nsMibVersion, nsRoot=nsRoot)

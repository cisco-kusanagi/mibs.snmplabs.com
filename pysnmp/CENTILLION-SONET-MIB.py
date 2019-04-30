#
# PySNMP MIB module CENTILLION-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-SONET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:30:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
atmSonet, = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "atmSonet")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Integer32, NotificationType, Counter64, IpAddress, TimeTicks, MibIdentifier, ModuleIdentity, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Integer32", "NotificationType", "Counter64", "IpAddress", "TimeTicks", "MibIdentifier", "ModuleIdentity", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmSonetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 4, 1))
cnSonetSectionTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 4, 1, 1), )
if mibBuilder.loadTexts: cnSonetSectionTable.setStatus('mandatory')
cnSonetSectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 4, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cnSonetSectionEntry.setStatus('mandatory')
cnSonetSectionBip8Errors = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 4, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnSonetSectionBip8Errors.setStatus('mandatory')
mibBuilder.exportSymbols("CENTILLION-SONET-MIB", atmSonetConfig=atmSonetConfig, cnSonetSectionTable=cnSonetSectionTable, cnSonetSectionBip8Errors=cnSonetSectionBip8Errors, cnSonetSectionEntry=cnSonetSectionEntry)

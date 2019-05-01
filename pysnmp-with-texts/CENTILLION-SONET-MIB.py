#
# PySNMP MIB module CENTILLION-SONET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CENTILLION-SONET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:48:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
atmSonet, = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "atmSonet")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, TimeTicks, Integer32, ObjectIdentity, Counter32, ModuleIdentity, Bits, Unsigned32, NotificationType, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "TimeTicks", "Integer32", "ObjectIdentity", "Counter32", "ModuleIdentity", "Bits", "Unsigned32", "NotificationType", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atmSonetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 930, 2, 2, 4, 1))
cnSonetSectionTable = MibTable((1, 3, 6, 1, 4, 1, 930, 2, 2, 4, 1, 1), )
if mibBuilder.loadTexts: cnSonetSectionTable.setStatus('mandatory')
if mibBuilder.loadTexts: cnSonetSectionTable.setDescription('The Centillion SONET/SDH Section table.')
cnSonetSectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 930, 2, 2, 4, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cnSonetSectionEntry.setStatus('mandatory')
if mibBuilder.loadTexts: cnSonetSectionEntry.setDescription('An entry in the Centillion SONET/SDH Section table.')
cnSonetSectionBip8Errors = MibTableColumn((1, 3, 6, 1, 4, 1, 930, 2, 2, 4, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnSonetSectionBip8Errors.setStatus('mandatory')
if mibBuilder.loadTexts: cnSonetSectionBip8Errors.setDescription('Section Bit Interleaved Parity. Number of STS-3(c) frames with BIP-8 errors.')
mibBuilder.exportSymbols("CENTILLION-SONET-MIB", cnSonetSectionEntry=cnSonetSectionEntry, cnSonetSectionTable=cnSonetSectionTable, atmSonetConfig=atmSonetConfig, cnSonetSectionBip8Errors=cnSonetSectionBip8Errors)

#
# PySNMP MIB module ChrComIfSonetSonetPathXcIndexNext-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComIfSonetSonetPathXcIndexNext-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:34:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
chrComIfSonet, = mibBuilder.importSymbols("Chromatis-MIB", "chrComIfSonet")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, Integer32, Counter32, ObjectIdentity, IpAddress, ModuleIdentity, iso, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Integer32", "Counter32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "iso", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Gauge32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComIfSonetSonetPathXcIndexNextTable = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComIfSonetSonetPathXcIndexNextTable.setStatus('current')
if mibBuilder.loadTexts: chrComIfSonetSonetPathXcIndexNextTable.setDescription('SonetPathXcIndexNext')
mibBuilder.exportSymbols("ChrComIfSonetSonetPathXcIndexNext-MIB", chrComIfSonetSonetPathXcIndexNextTable=chrComIfSonetSonetPathXcIndexNextTable)

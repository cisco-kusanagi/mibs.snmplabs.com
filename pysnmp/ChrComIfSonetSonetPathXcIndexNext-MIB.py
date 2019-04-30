#
# PySNMP MIB module ChrComIfSonetSonetPathXcIndexNext-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrComIfSonetSonetPathXcIndexNext-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:19:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
chrComIfSonet, = mibBuilder.importSymbols("Chromatis-MIB", "chrComIfSonet")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Gauge32, ObjectIdentity, Counter32, Counter64, Bits, IpAddress, MibIdentifier, Integer32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter32", "Counter64", "Bits", "IpAddress", "MibIdentifier", "Integer32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComIfSonetSonetPathXcIndexNextTable = MibScalar((1, 3, 6, 1, 4, 1, 3695, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chrComIfSonetSonetPathXcIndexNextTable.setStatus('current')
mibBuilder.exportSymbols("ChrComIfSonetSonetPathXcIndexNext-MIB", chrComIfSonetSonetPathXcIndexNextTable=chrComIfSonetSonetPathXcIndexNextTable)

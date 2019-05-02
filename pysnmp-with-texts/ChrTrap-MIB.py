#
# PySNMP MIB module ChrTrap-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrTrap-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:36:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
chrComTrap, = mibBuilder.importSymbols("Chromatis-MIB", "chrComTrap")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, NotificationType, iso, TimeTicks, NotificationType, Counter64, Counter32, Integer32, ObjectIdentity, Gauge32, ModuleIdentity, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "iso", "TimeTicks", "NotificationType", "Counter64", "Counter32", "Integer32", "ObjectIdentity", "Gauge32", "ModuleIdentity", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComTrapLoggedTrap = NotificationType((1, 3, 6, 1, 4, 1, 3695, 1, 6) + (0,1))
if mibBuilder.loadTexts: chrComTrapLoggedTrap.setDescription('This trap informs about a new event that was reported to the TrapLog table.')
mibBuilder.exportSymbols("ChrTrap-MIB", chrComTrapLoggedTrap=chrComTrapLoggedTrap)

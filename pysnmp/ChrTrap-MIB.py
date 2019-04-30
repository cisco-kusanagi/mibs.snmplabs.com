#
# PySNMP MIB module ChrTrap-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ChrTrap-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:20:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
chrComTrap, = mibBuilder.importSymbols("Chromatis-MIB", "chrComTrap")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, NotificationType, Bits, iso, Counter32, ObjectIdentity, Counter64, Gauge32, IpAddress, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "NotificationType", "Bits", "iso", "Counter32", "ObjectIdentity", "Counter64", "Gauge32", "IpAddress", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chrComTrapLoggedTrap = NotificationType((1, 3, 6, 1, 4, 1, 3695, 1, 6) + (0,1))
mibBuilder.exportSymbols("ChrTrap-MIB", chrComTrapLoggedTrap=chrComTrapLoggedTrap)

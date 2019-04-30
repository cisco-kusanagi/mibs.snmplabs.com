#
# PySNMP MIB module REDUND-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDUND-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
sysMcpRedundOperState, sysMcpRedundIndx = mibBuilder.importSymbols("CENTILLION-CONFIG-MIB", "sysMcpRedundOperState", "sysMcpRedundIndx")
sysMcpRedundTrap, = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "sysMcpRedundTrap")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, iso, Integer32, Counter32, NotificationType, MibIdentifier, Unsigned32, Bits, TimeTicks, IpAddress, NotificationType, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "iso", "Integer32", "Counter32", "NotificationType", "MibIdentifier", "Unsigned32", "Bits", "TimeTicks", "IpAddress", "NotificationType", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sysMcpRedundDown = NotificationType((1, 3, 6, 1, 4, 1, 930, 2, 1, 4, 1) + (0,1)).setObjects(("CENTILLION-CONFIG-MIB", "sysMcpRedundIndx"), ("CENTILLION-CONFIG-MIB", "sysMcpRedundOperState"))
mibBuilder.exportSymbols("REDUND-TRAP-MIB", sysMcpRedundDown=sysMcpRedundDown)

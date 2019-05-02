#
# PySNMP MIB module REDUND-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDUND-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
sysMcpRedundIndx, sysMcpRedundOperState = mibBuilder.importSymbols("CENTILLION-CONFIG-MIB", "sysMcpRedundIndx", "sysMcpRedundOperState")
sysMcpRedundTrap, = mibBuilder.importSymbols("CENTILLION-ROOT-MIB", "sysMcpRedundTrap")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, ObjectIdentity, Gauge32, MibIdentifier, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Integer32, NotificationType, iso, TimeTicks, Unsigned32, Counter32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "ObjectIdentity", "Gauge32", "MibIdentifier", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Integer32", "NotificationType", "iso", "TimeTicks", "Unsigned32", "Counter32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sysMcpRedundDown = NotificationType((1, 3, 6, 1, 4, 1, 930, 2, 1, 4, 1) + (0,1)).setObjects(("CENTILLION-CONFIG-MIB", "sysMcpRedundIndx"), ("CENTILLION-CONFIG-MIB", "sysMcpRedundOperState"))
if mibBuilder.loadTexts: sysMcpRedundDown.setDescription("When two MCP's are participating in redundancy, they are aware of each other through a mechanism based on heart beat protocol. When primary MCP detects the failure of the secondary, it will send the trap immediately. When the secondary MCP detects the primary has failed, it will take control, reset the switch and then send the trap. Varbind information returned with this trap: 1. sysMcpRedundIndx represents the slot where active MCP resides. 2. sysMcpRedundOperState represents the state of the failed MCP.")
mibBuilder.exportSymbols("REDUND-TRAP-MIB", sysMcpRedundDown=sysMcpRedundDown)

#
# PySNMP MIB module REMOTE-LOGIN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REMOTE-LOGIN-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:55:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
s5AgRemoteLoginIp, s5AgRemoteLoginStatus = mibBuilder.importSymbols("S5-AGENT-MIB", "s5AgRemoteLoginIp", "s5AgRemoteLoginStatus")
remoteLoginTrap, = mibBuilder.importSymbols("S5-ROOT-MIB", "remoteLoginTrap")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Unsigned32, MibIdentifier, iso, Counter32, Integer32, NotificationType, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Bits, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "MibIdentifier", "iso", "Counter32", "Integer32", "NotificationType", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Bits", "Counter64", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
remoteLoginStatus = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 8) + (0,1)).setObjects(("S5-AGENT-MIB", "s5AgRemoteLoginIp"), ("S5-AGENT-MIB", "s5AgRemoteLoginStatus"))
if mibBuilder.loadTexts: remoteLoginStatus.setDescription(' This trap is sent when someone login via telnet. The status of login and the host ip are reported together.')
mibBuilder.exportSymbols("REMOTE-LOGIN-TRAP-MIB", remoteLoginStatus=remoteLoginStatus)

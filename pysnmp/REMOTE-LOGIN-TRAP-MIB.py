#
# PySNMP MIB module REMOTE-LOGIN-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REMOTE-LOGIN-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
s5AgRemoteLoginIp, s5AgRemoteLoginStatus = mibBuilder.importSymbols("S5-AGENT-MIB", "s5AgRemoteLoginIp", "s5AgRemoteLoginStatus")
remoteLoginTrap, = mibBuilder.importSymbols("S5-ROOT-MIB", "remoteLoginTrap")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Integer32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, IpAddress, MibIdentifier, NotificationType, ModuleIdentity, ObjectIdentity, Bits, TimeTicks, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "IpAddress", "MibIdentifier", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Bits", "TimeTicks", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
remoteLoginStatus = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 8) + (0,1)).setObjects(("S5-AGENT-MIB", "s5AgRemoteLoginIp"), ("S5-AGENT-MIB", "s5AgRemoteLoginStatus"))
mibBuilder.exportSymbols("REMOTE-LOGIN-TRAP-MIB", remoteLoginStatus=remoteLoginStatus)

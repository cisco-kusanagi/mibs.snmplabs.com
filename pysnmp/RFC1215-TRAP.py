#
# PySNMP MIB module RFC1215-TRAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RFC1215-TRAP
# Produced by pysmi-0.3.4 at Mon Apr 29 20:48:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
egpNeighAddr, = mibBuilder.importSymbols("RFC1213-MIB", "egpNeighAddr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
snmp, = mibBuilder.importSymbols("SNMPv2-MIB", "snmp")
Gauge32, Bits, MibIdentifier, ObjectIdentity, Unsigned32, Integer32, NotificationType, TimeTicks, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, ModuleIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Integer32", "NotificationType", "TimeTicks", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "ModuleIdentity", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
coldStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,0))
warmStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,1))
linkDown = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,2)).setObjects(("IF-MIB", "ifIndex"))
linkUp = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,3)).setObjects(("IF-MIB", "ifIndex"))
authenticationFailure = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,4))
egpNeighborLoss = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,5)).setObjects(("RFC1213-MIB", "egpNeighAddr"))
mibBuilder.exportSymbols("RFC1215-TRAP", egpNeighborLoss=egpNeighborLoss, linkUp=linkUp, linkDown=linkDown, coldStart=coldStart, warmStart=warmStart, authenticationFailure=authenticationFailure)

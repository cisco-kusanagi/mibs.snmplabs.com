#
# PySNMP MIB module RFC1215-TRAP (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RFC1215-TRAP
# Produced by pysmi-0.3.4 at Wed May  1 14:56:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
egpNeighAddr, = mibBuilder.importSymbols("RFC1213-MIB", "egpNeighAddr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
snmp, = mibBuilder.importSymbols("SNMPv2-MIB", "snmp")
NotificationType, Integer32, TimeTicks, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, iso, ObjectIdentity, IpAddress, MibIdentifier, Bits, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "TimeTicks", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "iso", "ObjectIdentity", "IpAddress", "MibIdentifier", "Bits", "NotificationType", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
coldStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,0))
if mibBuilder.loadTexts: coldStart.setDescription("A coldStart trap signifies that the sending protocol entity is reinitializing itself such that the agent's configuration or the protocol entity implementation may be altered.")
warmStart = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,1))
if mibBuilder.loadTexts: warmStart.setDescription('A warmStart trap signifies that the sending protocol entity is reinitializing itself such that neither the agent configuration nor the protocol entity implementation is altered.')
linkDown = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,2)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: linkDown.setDescription("A linkDown trap signifies that the sending protocol entity recognizes a failure in one of the communication links represented in the agent's configuration.")
linkUp = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,3)).setObjects(("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: linkUp.setDescription("A linkUp trap signifies that the sending protocol entity recognizes that one of the communication links represented in the agent's configuration has come up.")
authenticationFailure = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,4))
if mibBuilder.loadTexts: authenticationFailure.setDescription('An authenticationFailure trap signifies that the sending protocol entity is the addressee of a protocol message that is not properly authenticated. While implementations of the SNMP must be capable of generating this trap, they must also be capable of suppressing the emission of such traps via an implementation-specific mechanism.')
egpNeighborLoss = NotificationType((1, 3, 6, 1, 2, 1, 11) + (0,5)).setObjects(("RFC1213-MIB", "egpNeighAddr"))
if mibBuilder.loadTexts: egpNeighborLoss.setDescription('An egpNeighborLoss trap signifies that an EGP neighbor for whom the sending protocol entity was an EGP peer has been marked down and the peer relationship no longer obtains.')
mibBuilder.exportSymbols("RFC1215-TRAP", coldStart=coldStart, linkUp=linkUp, egpNeighborLoss=egpNeighborLoss, linkDown=linkDown, authenticationFailure=authenticationFailure, warmStart=warmStart)

#
# PySNMP MIB module ATM-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATM-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:31:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
atmPortPortIndex, atmPortCardIndex, atmPortSscopStatus = mibBuilder.importSymbols("CENTILLION-ATMCFG-MIB", "atmPortPortIndex", "atmPortCardIndex", "atmPortSscopStatus")
atmTraps, = mibBuilder.importSymbols("S5-ROOT-MIB", "atmTraps")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Counter32, Gauge32, iso, NotificationType, TimeTicks, Unsigned32, Counter64, Integer32, NotificationType, Bits, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "Gauge32", "iso", "NotificationType", "TimeTicks", "Unsigned32", "Counter64", "Integer32", "NotificationType", "Bits", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
s5CtrSscopDown = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 7) + (0,1)).setObjects(("CENTILLION-ATMCFG-MIB", "atmPortCardIndex"), ("CENTILLION-ATMCFG-MIB", "atmPortPortIndex"), ("CENTILLION-ATMCFG-MIB", "atmPortSscopStatus"))
if mibBuilder.loadTexts: s5CtrSscopDown.setDescription(' This trap is sent when the SSCOP goes down i.e., when the peer protocol has failed to respond to the max number of status polls by its peer. atmPortCardIndex.........the ATM card id. atmPortPortIndex.........the ATM port id. atmPortSscopStatus ..........the status of the SSCOP protocol.')
s5CtrAdmaLockup = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 7) + (0,2)).setObjects(("CENTILLION-ATMCFG-MIB", "atmPortCardIndex"), ("CENTILLION-ATMCFG-MIB", "atmPortPortIndex"))
if mibBuilder.loadTexts: s5CtrAdmaLockup.setDescription(' This trap is sent when a ADMA lockup condition is detected on the MCP. The MCP must be reset to clear this condition. atmPortCardIndex.........the ATM card id. atmPortPortIndex.........the ATM port id.')
s5CtrAcmaLockup = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 7) + (0,3)).setObjects(("CENTILLION-ATMCFG-MIB", "atmPortCardIndex"))
if mibBuilder.loadTexts: s5CtrAcmaLockup.setDescription(' This trap is sent when a ACMA queue stuck condition is detected on the MCP. The MCP must be reset to clear this condition. atmPortCardIndex.........the ATM card id.')
mibBuilder.exportSymbols("ATM-TRAP-MIB", s5CtrAdmaLockup=s5CtrAdmaLockup, s5CtrSscopDown=s5CtrSscopDown, s5CtrAcmaLockup=s5CtrAcmaLockup)

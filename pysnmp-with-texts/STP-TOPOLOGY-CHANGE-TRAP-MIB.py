#
# PySNMP MIB module STP-TOPOLOGY-CHANGE-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STP-TOPOLOGY-CHANGE-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:11:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
bridgeGroupIdentifier, = mibBuilder.importSymbols("CENTILLION-BRIDGEGROUP-MIB", "bridgeGroupIdentifier")
stpChangeTrap, = mibBuilder.importSymbols("S5-ROOT-MIB", "stpChangeTrap")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, MibIdentifier, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, ModuleIdentity, Integer32, IpAddress, Counter64, TimeTicks, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "MibIdentifier", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "ModuleIdentity", "Integer32", "IpAddress", "Counter64", "TimeTicks", "Gauge32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stpRxTopologyChg = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 9) + (0,1)).setObjects(("CENTILLION-BRIDGEGROUP-MIB", "bridgeGroupIdentifier"))
if mibBuilder.loadTexts: stpRxTopologyChg.setDescription(' This trap is sent when a spanning tree group receives a topology change notification.')
mibBuilder.exportSymbols("STP-TOPOLOGY-CHANGE-TRAP-MIB", stpRxTopologyChg=stpRxTopologyChg)

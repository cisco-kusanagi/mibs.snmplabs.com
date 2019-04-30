#
# PySNMP MIB module STP-TOPOLOGY-CHANGE-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STP-TOPOLOGY-CHANGE-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:04:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
bridgeGroupIdentifier, = mibBuilder.importSymbols("CENTILLION-BRIDGEGROUP-MIB", "bridgeGroupIdentifier")
stpChangeTrap, = mibBuilder.importSymbols("S5-ROOT-MIB", "stpChangeTrap")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, MibIdentifier, Counter32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, Integer32, NotificationType, TimeTicks, Bits, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "MibIdentifier", "Counter32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "Integer32", "NotificationType", "TimeTicks", "Bits", "IpAddress", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
stpRxTopologyChg = NotificationType((1, 3, 6, 1, 4, 1, 45, 1, 6, 2, 9) + (0,1)).setObjects(("CENTILLION-BRIDGEGROUP-MIB", "bridgeGroupIdentifier"))
mibBuilder.exportSymbols("STP-TOPOLOGY-CHANGE-TRAP-MIB", stpRxTopologyChg=stpRxTopologyChg)

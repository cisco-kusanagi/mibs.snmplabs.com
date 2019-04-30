#
# PySNMP MIB module ATM-SOFT-PVC-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATM-SOFT-PVC-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:15:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
atmSoftPvcTrapsPrefix, atmSoftPvcCurrentlyFailingSoftPVpcs, atmSoftPvcCallFailures, atmSoftPvcCurrentlyFailingSoftPVccs = mibBuilder.importSymbols("ATM-SOFT-PVC-MIB", "atmSoftPvcTrapsPrefix", "atmSoftPvcCurrentlyFailingSoftPVpcs", "atmSoftPvcCallFailures", "atmSoftPvcCurrentlyFailingSoftPVccs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, ObjectIdentity, Counter64, Gauge32, TimeTicks, NotificationType, iso, Integer32, NotificationType, IpAddress, ModuleIdentity, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "Counter64", "Gauge32", "TimeTicks", "NotificationType", "iso", "Integer32", "NotificationType", "IpAddress", "ModuleIdentity", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmSoftPvcCallFailuresTrap = NotificationType((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1, 0) + (0,1)).setObjects(("ATM-SOFT-PVC-MIB", "atmSoftPvcCallFailures"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVccs"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVpcs"))
mibBuilder.exportSymbols("ATM-SOFT-PVC-TRAP-MIB", atmSoftPvcCallFailuresTrap=atmSoftPvcCallFailuresTrap)

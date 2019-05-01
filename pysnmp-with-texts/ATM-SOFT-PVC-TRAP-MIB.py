#
# PySNMP MIB module ATM-SOFT-PVC-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATM-SOFT-PVC-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:31:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
atmSoftPvcTrapsPrefix, atmSoftPvcCurrentlyFailingSoftPVpcs, atmSoftPvcCurrentlyFailingSoftPVccs, atmSoftPvcCallFailures = mibBuilder.importSymbols("ATM-SOFT-PVC-MIB", "atmSoftPvcTrapsPrefix", "atmSoftPvcCurrentlyFailingSoftPVpcs", "atmSoftPvcCurrentlyFailingSoftPVccs", "atmSoftPvcCallFailures")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, ObjectIdentity, IpAddress, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, NotificationType, TimeTicks, iso, MibIdentifier, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "NotificationType", "TimeTicks", "iso", "MibIdentifier", "Gauge32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmSoftPvcCallFailuresTrap = NotificationType((1, 3, 6, 1, 4, 1, 353, 5, 5, 1, 2, 1, 0) + (0,1)).setObjects(("ATM-SOFT-PVC-MIB", "atmSoftPvcCallFailures"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVccs"), ("ATM-SOFT-PVC-MIB", "atmSoftPvcCurrentlyFailingSoftPVpcs"))
if mibBuilder.loadTexts: atmSoftPvcCallFailuresTrap.setDescription('A notification indicating that one or more series of call attempts in trying to establish a Soft PVPC or Soft PVCC have failed since the last atmSoftPvcCallFailureTrap was sent. If this trap has not been sent for the last atmSoftPvcNotificationInterval, then it will be sent on the next increment of atmSoftPvcCallFailures.')
mibBuilder.exportSymbols("ATM-SOFT-PVC-TRAP-MIB", atmSoftPvcCallFailuresTrap=atmSoftPvcCallFailuresTrap)
